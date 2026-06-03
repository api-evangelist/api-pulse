#!/usr/bin/env python3
"""Generate Jekyll collection documents for API Pulse from the Naftiko Signals data set.

Reads the source YAML (companies, services, tools, standards) and writes one Markdown
document per item into the matching collection directory (_companies, _services, _tools,
_standards). Items missing a slug get one derived from their name; slug collisions are
de-duplicated with a numeric suffix.

Usage:
    python3 scripts/generate_collections.py [SOURCE_DATA_DIR]

SOURCE_DATA_DIR defaults to ../../signals-jobs/_data relative to the repo root.
"""
import os
import re
import sys
import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SRC = os.path.normpath(os.path.join(REPO_ROOT, "..", "..", "signals-jobs", "_data"))


def slugify(value):
    value = re.sub(r"[^\w\s-]", "", str(value).lower()).strip()
    value = re.sub(r"[\s_]+", "-", value)
    value = re.sub(r"-+", "-", value)
    return value or "item"


def unique_slug(base, used):
    slug = base
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def write_doc(path, front_matter):
    """Write a Jekyll doc with a YAML front-matter block and an empty body."""
    with open(path, "w") as f:
        f.write("---\n")
        f.write(yaml.safe_dump(front_matter, sort_keys=False, allow_unicode=True,
                               default_flow_style=False, width=10000))
        f.write("---\n")


def clean(d, keys):
    """Pick keys from d that are present and not None/empty."""
    out = {}
    for k in keys:
        v = d.get(k)
        if v is not None and v != "" and v != []:
            out[k] = v
    return out


def generate_adoption(src_file, out_dir):
    items = yaml.safe_load(open(src_file)) or []
    os.makedirs(out_dir, exist_ok=True)
    used = set()
    count = 0
    for item in items:
        name = item.get("name")
        if not name:
            continue
        base = item.get("slug") or slugify(name)
        slug = unique_slug(slugify(base), used)
        fm = {"title": name, "slug": slug}
        fm["companyCount"] = item.get("companyCount") or 0
        fm.update(clean(item, [
            "description", "tags", "url", "founded", "yearCreated",
            "radarRing", "alternativeNames",
        ]))
        write_doc(os.path.join(out_dir, slug + ".md"), fm)
        count += 1
    return count


def generate_companies(src_file, out_dir):
    data = yaml.safe_load(open(src_file)) or {}
    companies = data.get("common", [])
    os.makedirs(out_dir, exist_ok=True)
    used = set()
    count = 0
    for c in companies:
        name = c.get("name")
        if not name:
            continue
        base = c.get("slug") or slugify(name)
        slug = unique_slug(slugify(base), used)
        fm = {"title": name, "slug": slug}
        fm.update(clean(c, [
            "description", "tags", "industries", "url", "jobUrl",
            "apiEvangelistRepo", "has_signals",
        ]))
        # Flatten the richest signal fields into a compact, render-friendly shape.
        ls = c.get("lead_signals") or {}
        if ls:
            sig = {}
            if ls.get("total_signal_score") is not None:
                sig["total_signal_score"] = ls["total_signal_score"]
            for dim in ("ai_maturity", "data_maturity", "governance_maturity"):
                cls = (ls.get(dim) or {}).get("classification")
                if cls:
                    sig[dim] = cls
            bs = ls.get("buying_signals") or {}
            for k in ("activity_level", "jobs_count", "press_count"):
                if bs.get(k) is not None:
                    sig[k] = bs[k]
            if sig:
                fm["signals"] = sig
        pa = c.get("platform_affinity") or {}
        if pa:
            plat = clean(pa, ["cloud_primary", "cloud_classification", "productivity_stack"])
            if plat:
                fm["platform"] = plat
        write_doc(os.path.join(out_dir, slug + ".md"), fm)
        count += 1
    return count


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SRC
    if not os.path.isdir(src):
        sys.exit(f"Source data directory not found: {src}")
    print(f"Source: {src}")
    n = generate_companies(os.path.join(src, "companies.yml"),
                           os.path.join(REPO_ROOT, "_companies"))
    print(f"  companies: {n}")
    for name in ("services", "tools", "standards"):
        n = generate_adoption(os.path.join(src, name + ".yml"),
                              os.path.join(REPO_ROOT, "_" + name))
        print(f"  {name}: {n}")


if __name__ == "__main__":
    main()
