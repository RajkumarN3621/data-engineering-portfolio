from __future__ import annotations

from typing import Iterable

import pandas as pd


def row_count(df: pd.DataFrame) -> int:
    return len(df)


def null_percentage(df: pd.DataFrame, columns: Iterable[str]) -> dict[str, float]:
    return {
        column: round(float(df[column].isna().mean() * 100), 2)
        for column in columns
    }


def distinct_count(df: pd.DataFrame, columns: Iterable[str]) -> dict[str, int]:
    return {column: int(df[column].nunique(dropna=True)) for column in columns}


def duplicate_count(df: pd.DataFrame, key_columns: list[str]) -> int:
    return int(df.duplicated(subset=key_columns, keep=False).sum())


def numeric_statistics(
    df: pd.DataFrame,
    columns: Iterable[str],
) -> dict[str, dict[str, float]]:
    result = {}

    for column in columns:
        series = pd.to_numeric(df[column], errors="coerce")
        result[column] = {
            "count": int(series.count()),
            "min": float(series.min()),
            "max": float(series.max()),
            "mean": round(float(series.mean()), 2),
            "sum": float(series.sum()),
        }

    return result
