# spotify-data-cleaning
A Python project dedicated to cleaning, transforming, and structuring messy public data.
# Spotify Data Cleaning Pipeline 🎵

## Project Objective
This project takes raw, unformatted public Spotify streaming data and utilizes Python (Pandas) to clean, handle missing data structures, and format data types for downstream analytical use.

## The Logic Step-by-Step
* **Ingestion:** Loaded a raw dataset containing over 50k unverified tracking rows.
* **Handling Nulls:** Dropped missing critical values and handled optional features using median imputations.
* **Deduplication:** Stripped duplicate unique identifiers to prevent skewed metrics.
* **Type Conversion:** Formatted absolute timestamps into standardized ISO `datetime` blocks.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install pandas`
3. Execute `python clean.py` to process the raw matrix.
