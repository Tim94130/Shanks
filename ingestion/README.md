# Ingestion Engine

This module handles data ingestion from various sources (Unity, KAT, PCS, TDC, SerOM).

## Structure

- `app/jobs/`: Specific logic for each data source.
- `app/pipelines/`: Orchestration of extraction, transformation, and loading.
- `app/common/`: Shared utilities for parsing and normalization.
- `app/output/`: Destination formats for the API.

## Usage

Run a specific job:
```bash
python -m app.jobs.unity.main
```
