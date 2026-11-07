#!/usr/bin/env python3

"""
Fetch screen scores in json format, and load the results
into a polars dataframe. Polars is a fast dataframe library
with an expression-based API for filtering and transforming data.

This mirrors get_screen_pandas.py step for step, so you can compare the two.
"""

import httpx
import polars as pl
from loguru import logger

from core import config as cfg


def main() -> None:
    screen_id = 205
    request_url = f"{cfg.BASE_URL}/screen/{screen_id}"

    # These parameters can be modified to match any search criteria following
    # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
    # In this particular case, we've chosen to return everything in the json format.
    params = {
        "accesskey": cfg.ACCESS_KEY,
        "format": "json",
    }

    response = httpx.get(request_url, params=params, timeout=30)
    response.raise_for_status()
    screen = response.json()

    # Load the list of rows into a polars dataframe.
    # Polars has no row index like pandas, so IDENTIFIER_ID stays a regular column.
    dataset = pl.DataFrame(screen)

    # Keep only the columns we care about
    columns = [
        "IDENTIFIER_ID",
        "IDENTIFIER_TYPE",
        "OFFICIAL_SYMBOL",
        "ALIASES",
        "ORGANISM_ID",
        "ORGANISM_OFFICIAL",
        "SCORE.1",
        "SCORE.2",
        "HIT",
        "SOURCE",
    ]
    dataset = dataset.select(columns)

    # Convert score columns into numbers. The API uses "-" for a missing score,
    # and strict=False turns those into null instead of raising an error.
    dataset = dataset.with_columns(
        pl.col("SCORE.1").cast(pl.Float64, strict=False),
        pl.col("SCORE.2").cast(pl.Float64, strict=False),
    )

    # Show all rows with SCORE.1 > 1
    logger.info("Rows with SCORE.1 > 1:\n{}", dataset.filter(pl.col("SCORE.1") > 1))

    # Show hits only
    logger.info("Hits only:\n{}", dataset.filter(pl.col("HIT") == "YES"))


if __name__ == "__main__":
    main()
