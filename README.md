# Analytics Copilot Runtime

> Repository: 1325863889-design/analytics-copilot-runtime  
> Status: portfolio-ready source package

## Overview

A semantic analytics copilot runtime for SQL generation, metric recall, schema reasoning, and natural-language data exploration.

The repository is organized as a source-first engineering project. Local datasets, model weights, environment files, binary installers, generated outputs, and bulky media archives are intentionally excluded from version control. When those assets are required, keep them in external storage and document the download or provisioning process.

## Capabilities

- Question understanding and SQL planning
- Metric, table, and field recall
- Prompt assets for SQL generation and correction
- Infrastructure recipes for analytics services

## Technology Stack

Python, SQL, Docker Compose, MySQL, Elasticsearch, LLM services

## Repository Layout

- src/: application source, services, scripts, or runtime package code.
- docs/: architecture notes, diagrams, and implementation references.
- data/: lightweight sample data or schema files that are safe to version.
- infra/: Docker, database, or service-bootstrap configuration.
- prompts/: prompt templates and LLM workflow assets.
- ssets/: UI, image, diagram, or static resources.
- examples/: iteration snapshots, demos, or reference implementations.
- esources/: supporting files that do not fit the categories above.

## Local Setup

Configure services from `infra/docker`, review prompt assets under `prompts`, then run the application code from `src` or the latest snapshot under `examples`.

General setup checklist:

1. Create a Python or Node environment based on the dependency files in src or examples.
2. Copy .env.example to .env if an example file is provided, then fill in local service credentials.
3. Start required backing services such as MySQL, Neo4j, Milvus, MinIO, Elasticsearch, or model APIs.
4. Run the smallest backend script, API entrypoint, or test workflow before starting the complete application.

## Data and Model Artifacts

The following assets are intentionally not committed:

- API keys, database passwords, and local .env files.
- Virtual environments, dependency folders, caches, logs, and generated outputs.
- Model checkpoints, pretrained weights, TensorBoard runs, and large binary artifacts.
- Private business data, bulky datasets, media archives, and installer packages.

For production use, store large assets in Git LFS, object storage, Hugging Face, ModelScope, or an internal artifact registry.

## Maintenance Notes

- Add .env.example files for services that require configuration.
- Pin runtime dependencies once the deployment target is fixed.
- Add smoke tests for the primary service entrypoints.
- Keep sample data small and move bulky artifacts outside Git.