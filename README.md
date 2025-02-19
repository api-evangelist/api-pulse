# The API Pulse
This is a proposed schema for publishing to the API Pulse using an HTTP API, capturing a snapshot of how APIs are being used across industries around the globe by the people who are producing and consuming them.

## Overview ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/1))
The API industry is in need of accessible community data that helps share knowledge about how everyone is using APIs while prioritizing the following dimensions of what we need for our API operations.

- **Vendor Neutral** - You aren't to be sold to as part of engagement.
- **API-First** - Defined as an API first, then develop applications.
- **Across Industries** - Understanding across, but also within industries.
- **Across Countries** - Allowing for understanding usage in countries.
- **Across Signals** - Look at APIs, but also the other common signals.
- **Bi-Annual Reports** - Summarizing and publishing reports twice a year.
- **Ongoing Pulse Checks** - Anyone contributing gets ongoing pulse checks.

## Goals ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/2))
The goal of the API Pulse is to help organizations and individuals better understand the industries they operate in, or are planning on moving into, helping inform career and business decisions.

- **Position in Existing Industries**
- **State of Existing Industries**
- **Awareness of New Industries**
- **Education of Common Practices**

## Schema
The schema for the API pulse is currently defined as [an OpenAPI 3.1 that uses the latest draft of JSON Schema](https://github.com/api-evangelist/api-pulse/blob/main/openapi/api-pulse-publish-openapi.yml) to define the schema for each API pulse signal and how it can be submitted.

### People ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L899)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/3))
Pulse of the API people.

- **name** - A name.
- **email** - Valid email address.
- **role** - Role of the person.
- **linkedIn** - Valid LinkedIn URL.
- **countries** - A valid ISO 3166 country.
- **other** - Other information (People).

### Organization ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L948)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/4))
Pulse of the API organization.

- **email** - A valid email (Organization).
- **countries** - A valid ISO 3166 country.
- **industries** - A valid North American Industry Classification System (NAICS) entry.
- **employees** - The number of employees that work at an enterprise organization.
- **other** - Other information (Organization).

### Access ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L992)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/5))
Pulse of API access.

- **email** - A valid email (Access).
- **internal** - How many internal APIs do you produce?
- **partner** - How many partner APIs do you produce?
- **public** - How many public APIs do you produce?
- **other** - Other information (Access).

### Distribution ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1031)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/6))
Pulse of API distribution.

- **email** - A valid email (Distribution).
- **publicPortal** - How many public API portals do you have?
- **internalPortal** - How many internal API portals do you have?
- **gateway** - How many API gateways do you have?
- **other** - Other information (Distribution).

### Authentication ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1068)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/7))
Pulse of API authentication.

- **email** - A valid email (Authentication).
- **basicAuth** - Do you use BasicAuth to authenticate with APIs?
- **keys** - Do you use API keys to authenticate with APIs?
- **jwt** - Do you use JWT to authenticate with APIs?
- **oauth** - Do you use OAuth to authenticate with APIs?
- **other** - Other information (Authentication).

### HttpApi ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1106)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/8))
Pulse of HTTP APIs.

- **email** - A valid email (HTTP API).
- **producedCount** - How many HTTP APIs do you produce?
- **producedPercentage** - What percentage of APIs you produce are HTTP APIs?
- **consumeCount** - How many HTTP APIs do you consume?
- **consumePercentage** - What percentage of APIs you consume are HTTP APIs?
- **openApi** - Do you use OpenAPI?
- **designFirst** - Are you design-first when producing HTTP APIs?
- **openApiDocumentation** - Do you use OpenAPI for Generating Documentation?
- **openApiMockServers** - Do you use OpenAPI for Generating Mock Servers?
- **openApiSdks** - Do you use OpenAPI for Software Development Kits (SDKs)?
- **openApiTesting** - Do you use OpenAPI for Testing?
- **openApiSecurity** - Do you use OpenAPI for Security?
- **openApiPortal** - Do you publish OpenAPI to a portal?
- **openApiRespository** - Do you publish OpenAPI to a repository?
- **other** - Other information (HTTP APIs).

### GraphQlApi ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1197)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/9))
Pulse of GraphQL APIs.

- **email** - A valid email (GraphQL API).
- **producedCount** - How many GraphQL APIs do you produce?
- **producedPercentage** - What percentage of the  APIs you produce are GraphQL?
- **consumeCount** - How many GraphQL APIs do you consume?
- **consumePercentage** - What percentage of the APIs you consume are GraphQL APIs?
- **internally** - Do you use GraphQL internally?
- **externally** - Do you use GraphQL externally?
- **other** - Other information (GraphQL APIs).

### EventDrivenApi ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1253)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/10))
Pulse of Event-Driven APIs.

- **email** - A valid email (Event-Driven).
- **webhooksPublish** - How many Webhooks do you publish?
- **webhooksSubscribe** - How many Webhooks do you subscribe to?
- **webSocketsProduce** - How many WebSockets do you produce?
- **webSocketsPublish** - How many WebSockets do you publish to?
- **webSocketsSubscribe** - How many WebSockets do you subscribe to?
- **kafkaProduce** - How many Kafka APIs do you produce?
- **kafkaPublish** - How many Kafka APIs do you publish to?
- **kafkaSubscribe** - How many Kafka APIs do you subscribe to?
- **asyncApi** - Do you use AsyncAPI?
- **designFirst** - Are you design-first when producing event-driven APIs?
- **asyncApiDocumentation** - Do you use AsyncAPI for Generating Documentation?
- **asyncApiMockServers** - Do you use AsyncAPI for Generating Mock Servers?
- **asyncApiSdks** - Do you use AsyncAPI for Software Development Kits (SDKs)?
- **asyncApiTesting** - Do you use AsyncAPI for Testing?
- **asyncApiSecurity** - Do you use AsyncAPI for Security?
- **asyncApiPortal** - Do you publish AsyncAPI to a portal?
- **asyncApiRespositor**y - Do you publish AsyncAPI to a repository?
- **other** - Other information (Event-Driven APIs).

### Schema ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1372)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/11))
Pulse of API schema.

- **email** - A valid email (Schema).
- **data** - Do you use JSON Schema to define data?
- **apis** - Do you use JSON Schema to define APIs?
- **validation** - Do you use JSON Schema to validate data?
- **forms** - Do you use JSON Schema to generate forms?
- **registry** - Do you publish a JSON Schema to the registry?
- **repository** - Do you publish the JSON Schema to the repository?
- **other** - Other information (Schema).

### Contracts ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1420)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/12))
Pulse of API discovery.

- **email** - A valid email (Contract).
- **discovery** - Do you use APIs.json for discovery?
- **portal** - Do you publish APIs.json to the portal?
- **repository** - Do you publish APIs.json to the repository?
- **other** - Other information (Contract).

### Experience ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1454)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/13))
Pulse of API experience.

- **email** - A valid email (Experience).
- **discovery** - How much of a priority is API discovery?
- **onboarding** - How much of a priority is API onboarding?
- **quality** - How much of a priority is API quality?
- **reliability** - How much of a priority is API reliability?
- **consistency** - How much of a priority is API consistency?
- **communication** - How much of a priority is API communication?
- **automation** - How much of a priority is API automation?
- **integration** - How much of a priority is API integration?
- **other** - Other information (Experience).

### Properties ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1526)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/14))
Pulse of API properties.

- **email** - A valid email (Properties).
- **documentation** - How much of a priority is API documentation?
- **mockServers** - How much of a priority is API mock servers?
- **sdks** - How much of a priority are SDKs?
- **testing** - How much of a priority is API testing?
- **security** - How much of a priority is API security?
- **versioning** - How much of a priority is API versioning?
- **other** - Other information (Properties).

### Plan ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1585)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/15))
Pulse of API plans.

- **email** - A valid email (Plan).
- **applications** - Do you require an application to be defined to access APIs?
- **rateLimits** - Do you enforce rate limits across all APIs?
- **chargeAccess** - Do you charge for access to any APIs?
- **usage** - Do you monitor API usage for APIs in production?
- **report** - Do you report on API usage data with consumers?
- **other** - Other information (Plan).

### Governance ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1628)) ([Discussion](https://github.com/api-evangelist/api-pulse/discussions/16))
Pulse of API governance.

- **email** - A valid email (Governance).
- **spectral** - Do you use Spectral for governance rules?
- **vacuum** - Do you use Vacuum for governance?
- **design** - Do you apply rules during the design of APIs?
- **development** - Do you apply rules during development of APIs?
- **pipelines** - Do you apply rules during pipeline builds of APIs?
- **gateway** - Do you validate JSON Schema at the API gateway?
- **other** - Other information (Governance).

## Accounts
The goal of the API Pulse is to allow you to use your personal or professional email to contribute one or more signals to the API pulse which matter most to you without setting up yet another account or assuming you use an existing service.

## Emails
Your email is only used to verify your pulse signals are coming from you, provide you access to regular API Pulse Checks, and send you our monthly newsletter--your email will not be sold or shared with any partners.

## Inclusive
The API Pulse works to be relevant to companies, organizations, institutions, and government agencies, but also to individuals--you can be design-first or code-first, producing or consuming APIs, and be a business or technical stakeholder.

## Scope
The first iteration of the API Pulse is trying to remain as simple and straightforward as possible, while focusing on just the fundamentals of API operations across many different industries--we can always expand the scope with future iterations.

## Checks
A separate API schema will soon be provided for checking the API Pulse in an ongoing way, allowing those who contribute to the API Pulse to check where they stand as individuals and organizations within the industries they contribute to.

## Reports
A separate API schema will soon be provided for pull spring and fall publishing of reports, allowing any to see the API pulse as submitted across all signals, countries, and industries, helping bring more awareness to the space.

### Report Target Dates

- May 2025
- September 2025

## Feedback
Feedback on the API Pulse schema can be made via four separate channels, allowing you to contribute to what data is published and available to subscribe to as part of regular checks and bi-annual reports.

- [GitHub Discussions](https://github.com/api-evangelist/api-pulse/discussions) - Where most of the conversation will occur.
- [GitHub Issues](https://github.com/api-evangelist/api-pulse/issues) - Submit an issue with any questions or comments.
- [Pull Request](https://github.com/api-evangelist/api-pulse/pulls) - Submit  a pull request making changes you want.
- [Email](mailto:info@apievangelist.com) - Drop us an email with questions.

Ideally feedback and questions remain openly accessible as issues and pull requests, but we understand not everyone will want to work out in the open and invite email communications, but please make sure and check the issues before emailing.