"""Chunked Redshift loading pattern.

The production pattern calculated chunk size from dataframe memory usage,
split the dataframe into manageable batches, and used parallel workers.
This version intentionally contains no client infrastructure.
"""

from concurrent.futures import ThreadPoolExecutor
import pandas as pd


def calculate_chunk_size(
    df: pd.DataFrame,
    max_sql_bytes: int = 15 * 1024 * 1024,
) -> int:
    if df.empty:
        return 1

    bytes_per_row = df.memory_usage(index=False, deep=True).sum() / len(df)
    return max(1, int(max_sql_bytes / bytes_per_row))


def split_dataframe(df: pd.DataFrame, chunk_size: int):
    for start in range(0, len(df), chunk_size):
        yield df.iloc[start:start + chunk_size]


def load_chunk(chunk: pd.DataFrame, chunk_number: int) -> int:
    print(f"Loading chunk {chunk_number}: {len(chunk):,} rows")
    return len(chunk)


def load_dataframe(df: pd.DataFrame, workers: int = 4) -> int:
    chunk_size = calculate_chunk_size(df)
    chunks = list(split_dataframe(df, chunk_size))

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(load_chunk, chunk, i + 1)
            for i, chunk in enumerate(chunks)
        ]
        loaded = sum(f.result() for f in futures)

    print(
        f"Loaded {loaded:,} rows across {len(chunks)} chunks "
        f"(chunk_size={chunk_size:,})"
    )
    return loaded
