#!/usr/bin/env python3

"""
Fetch screen scores in json format, and load the results
into a pandas dataframe. Pandas is a convenient library for
loading tabular datasets and provides the ability to perform
subsequent queries on the loaded dataframe after the fact.

See get_screen_polars.py for the same example using polars.
"""

import httpx
import pandas as pd
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

    # Load the list of rows into a pandas dataframe, indexed by gene identifier
    dataset = pd.DataFrame(screen).set_index("IDENTIFIER_ID")

    # Keep only the columns we care about
    columns = [
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
    dataset = dataset[columns]

    # Convert score columns into numbers. The API uses "-" for a missing score,
    # and errors="coerce" turns those into NaN instead of raising an error.
    for column in ["SCORE.1", "SCORE.2"]:
        dataset[column] = pd.to_numeric(dataset[column], errors="coerce")

    # Show all rows with SCORE.1 > 1
    logger.info("Rows with SCORE.1 > 1:\n{}", dataset[dataset["SCORE.1"] > 1])

    # Show hits only
    logger.info("Hits only:\n{}", dataset[dataset["HIT"] == "YES"])


if __name__ == "__main__":
    main()

"""
Output as of version 1.0.1 (rows with SCORE.1 > 1):
          IDENTIFIER_TYPE OFFICIAL_SYMBOL                              ALIASES ORGANISM_ID ORGANISM_OFFICIAL   SCORE.1  SCORE.2 HIT        SOURCE
100302736            gene    TMED7-TICAM2                                    -        9606      Homo sapiens  1.007427    0.382  NO  BioGRID ORCS
11235                gene          PDCD10                          CCM3|TFAR15        9606      Homo sapiens  1.007427    0.382  NO  BioGRID ORCS
154791               gene            FMC1                      C7orf55|HSPC268        9606      Homo sapiens  1.138414    0.382  NO  BioGRID ORCS
729873               gene          TBC1D3  PRC17|TBC1D3A|TBC1D3F|DKFZp434P2235        9606      Homo sapiens  2.968792    0.382  NO  BioGRID ORCS

Output as of version 1.0.1 (hits only):
         IDENTIFIER_TYPE OFFICIAL_SYMBOL                                            ALIASES ORGANISM_ID ORGANISM_OFFICIAL   SCORE.1  SCORE.2  HIT        SOURCE
10001                gene            MED6                                    ARC33|NY-REN-28        9606      Homo sapiens -0.779074  0.00721  YES  BioGRID ORCS
100049587            gene        SIGLEC14                                                  -        9606      Homo sapiens -0.545794  0.02040  YES  BioGRID ORCS
100287932            gene          TIMM23                                              TIM23        9606      Homo sapiens -0.587844  0.01160  YES  BioGRID ORCS
10036                gene          CHAF1A                     CAF-1|CAF1|CAF1B|CAF1P150|P150        9606      Homo sapiens -1.175897  0.00000  YES  BioGRID ORCS
...                   ...             ...                                                ...         ...               ...       ...      ...  ...           ...
"""  # noqa: E501
