# Privacy and data access

## Bundled data

This plugin bundles only blank templates, workflow instructions, and local Python scripts. It does not bundle real user profiles, project records, memory candidates, exports, credentials, account identifiers, contact details, or environment-specific configuration.

## Network and external services

The bundled scripts do not make network requests, send telemetry, call remote APIs, read browser data, or configure cloud synchronization.

## Local file access

The initializer:

- reads templates bundled inside the Skill;
- accepts a target path and a display label supplied by the user;
- requires the target path not to exist;
- writes the generated workspace only to that new target path;
- uses a temporary sibling directory during creation and removes only that temporary directory if creation fails.

The validator:

- reads the required Markdown files in the user-selected workspace;
- checks filenames under that workspace for sensitive-looking names;
- reports results locally;
- does not scan file contents for credentials and does not upload results.

## User responsibility

Do not place passwords, tokens, API keys, private keys, `.env` contents, contact details, full addresses, identity numbers, or unnecessary account identifiers in external memory. Review any filled memory workspace manually before sharing it.
