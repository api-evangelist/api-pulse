# API Pulse
This is a proposed schema for publishing to the API Pulse that captures a snapshot of how APIs are used across industries. 

## Background
The API industry is in need of data that helps share how everyone is using APIs, but prioritizes the following elements.

- **Vendor Neutral**
- **API-First**
- **Across Industries**
- **Across Countries**
- **Across Signals**
- **Twice Year Reports**
- **Ongoing Pulse Checks**

## Goals
The goal of the API Pulse is to help organizations and individuals understand better understand the industries around them.

- **Position in Existing Industries**
- **State of Existing Industries**
- **Awareness of New Industries**
- **Introduction to Common Practices**

## Schema
The schema is currently defined as an OpenAPI 3.1 with JSON Schem which provides a machine-readable draft of the following signals.

### People ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L899))
Pulse of the people.

 - **name** - A name.
 - **email** - Valid email address.
 - **role** - Role of the person.
 - **linkedIn** - Valid LinkedIn URL.
 - **countries** - A valid ISO 3166 country.
 - **other** - Other information (People).

### Organization ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L948))
Pulse of the organization.

 - **email** - A valid email (Organization).
 - **countries** - A valid ISO 3166 country.
 - **industries** - A valid North American Industry Classification System (NAICS) entry.
 - **employees** - The number of employees that work at an enterprise organization.
 - **other** - Other information (Organization).

### Access ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L992))
Pulse of API access.

 - **email** - A valid email (Access).
 - **internal** - How many internal APIs do you produce?
 - **partner** - How many partner APIs do you produce?
 - **public** - How many public APIs do you produce?
 - **other** - Other information (Access).

### Distribution ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1031))
Pulse of API distribution.

 - **email** - A valid email (Distribution).
 - **publicPortal** - How many public API portals do you have?
 - **internalPortal** - How many internal API portals do you have?
 - **gateway** - How many API gateways do you have?
 - **other** - Other information (Distribution).

### Authentication ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1068))
Pulse of API authentication.

 - **email** - A valid email (Authentication).
 - **basicAuth** - Do you use BasicAuth to authenticate with APIs?
 - **keys** - Do you use API keys to authenticate with APIs?
 - **jwt** - HDo you use JWT to authenticate with APIs?
 - **oauth** - Do you use OAuth to authenticate with APIs?
 - **other** - Other information (Authentication).

### HttpApi ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1106))
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

### GraphQlApi ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1197))
Pulse of GraphQL APIs.

 - **email** - A valid email (GraphQL API).
 - **producedCount** - How many GraphQL APIs do you produce?
 - **producedPercentage** - What percentage of the  APIs you produce are GraphQL?
 - **consumeCount** - How many GraphQL APIs do you consume?
 - **consumePercentage** - What percentage of the APIs you consume are GraphQL APIs?
 - **internally** - Do you use GraphQL internally?
 - **externally** - Do you use GraphQL externally?
 - **other** - Other information (GraphQL APIs).

### EventDrivenApi ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1253))
Pulse of Event-Driven APIs.

 - **email** - A valid email (Event-Driven).
 - **webhooksPublish** - How many Webhooks to you publish?
 - **webhooksSubscribe** - How many Webhooks to you subscribe?
 - **webSocketsProduce** - How many WebSockets to you produce?
 - **webSocketsPublish** - How many WebSockets to you publish to?
 - **webSocketsSubscribe** - How many WebSockets to you subscribe to?
 - **kafkaProduce** - How many Kafka APIs to you produce?
 - **kafkaPublish** - How many Kafka APIs to you publish to?
 - **kafkaSubscribe** - How many Kafka APIs to you subscribe to?
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

### Schema ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1372))
Pulse of schema.

 - **email** - A valid email (Schema).
 - **data** - Do you use JSON Schema to define data?
 - **apis** - Do you use JSON Schema to define APIs?
 - **validation** - Do you use JSON Schema to validate data?
 - **forms** - Do you use JSON Schema to generate forms?
 - **registry** - Do you publish JSON Schema to registry?
 - **repository** - Do you publish JSON Schema to repository?
 - **other** - Other information (Schema).

### Contracts ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1420))
Pulse of API discovery.

 - **email** - A valid email (Contract).
 - **discovery** - Do you use APIs.json for discovery?
 - **portal** - Do you publish APIs.json to portal?
 - **repository** - Do you publish APIs.json to repository?
 - **other** - Other information (Contract).

### Experience ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1454))
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

### Properties ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1526))
Pulse of API properties.

 - **email** - A valid email (Properties).
 - **documentation** - How much of a priority is API documentation?
 - **mockServers** - How much of a priority is API mock servers?
 - **sdks** - How much of a priority is SDKs?
 - **testing** - How much of a priority is API testing?
 - **security** - How much of a priority is API security?
 - **versioning** - How much of a priority is API versioning?
 - **other** - Other information (Properties).

### Plan ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1585))
Pulse of API plans.

 - **email** - A valid email (Plan).
 - **applications** - Do you require an application to be defined to access APIs?
 - **rateLimits** - Do you enforce rate limits across all APIs?
 - **chargeAccess** - Do you charge for access to any APIs?
 - **usage** - Do you monitor API usage for APIs in production?
 - **report** - Do you report on API usage data with consumers?
 - **other** - Other information (Plan).

### Governance ([Schema](https://github.com/api-evangelist/api-pulse/blob/2faeec4ca43a1bd6c6015d853e60aa32280855e1/openapi/api-pulse-publish-openapi.yml#L1628))
Pulse of API governance.

 - **email** - A valid email (Governance).
 - **spectral** - Do you use Spectral for governance rules?
 - **vacuum** - Do you use Vacuum for governance?
 - **design** - Do you apply rules during design of APIs?
 - **development** - Do you apply rules during development of APIs?
 - **pipelines** - Do you apply rules during pipeline builds of APIs?
 - **gateway** - Do you validate JSON Schema at the API gateway?
 - **other** - Other information (Governance).

## Checks
A separate schema will provided for checking the API pulse in an ongoing way, allowing those who contribute to the API pulse to check where they stand as individual and organization withint he industries they contribute to.

## Reports
A separate schema will be provided for pull spring and fall publishing of reports, allowing any to see the API pulse as submitted across all signals, countries, and industries, helping bring more awareness to the space.

## Fedback
Feedback on the API Pulse schema can be made via three separate channels, allowing you to contribute to what data is published and available to subscribe to as part of checks and reports.

- GitHub Issues - Submit an issue with any quesitons or comments.
- Pull Request - Submit  a pull request making changes you want.
- Email - info@apievangelist.com - Drop us an email with questions.