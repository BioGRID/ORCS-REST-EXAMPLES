#!/usr/bin/env python3

"""
Fetch screen scores with customizable search criteria
that can be tailored to match your own requirements
in json format
"""

import httpx
from loguru import logger

from core import config as cfg


def main() -> None:
    screen_id = 178
    request_url = f"{cfg.BASE_URL}/screen/{screen_id}"

    # These parameters can be modified to match any search criteria following
    # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
    # In this particular instance, we've chosen to return results in json format and to limit
    # values in the SCORE.1 column to the range of 0.9 and 0.98
    params = {
        "accesskey": cfg.ACCESS_KEY,
        "format": "json",
        "score1min": 0.9,
        "score1max": 0.98,
    }

    response = httpx.get(request_url, params=params, timeout=30)
    response.raise_for_status()
    screen = response.json()

    # Create a lookup of results by gene identifier
    data = {}
    for row in screen:
        data[row["IDENTIFIER_ID"]] = row

    # Print out data about the genes BRIX1, ASB4, and NOB1
    for gene_id in ["55299", "51666", "28987"]:
        logger.info("Gene {}: {}", gene_id, data[gene_id])


if __name__ == "__main__":
    main()

"""
Output as of version 1.0.1:
{'IDENTIFIER_ID': '55299', 'IDENTIFIER_TYPE': 'gene', 'SCORE.3': '-', 'SCORE.2': '0.999965', 'SCORE.4': '-', 'SCORE.5': '-', 'SCORE.1': '0.94239', 'HIT': 'NO', 'SOURCE': 'BioGRID ORCS', 'SCREEN_ID': '178', 'ORGANISM_ID': '9606', 'OFFICIAL_SYMBOL': 'BRIX1', 'ALIASES': 'BRIX|BXDC2|FLJ11100', 'ORGANISM_OFFICIAL': 'Homo sapiens'}
{'IDENTIFIER_ID': '51666', 'IDENTIFIER_TYPE': 'gene', 'SCORE.3': '-', 'SCORE.2': '0.999965', 'SCORE.4': '-', 'SCORE.5': '-', 'SCORE.1': '0.97613', 'HIT': 'NO', 'SOURCE': 'BioGRID ORCS', 'SCREEN_ID': '178', 'ORGANISM_ID': '9606', 'OFFICIAL_SYMBOL': 'ASB4', 'ALIASES': 'ASB-4', 'ORGANISM_OFFICIAL': 'Homo sapiens'}
{'IDENTIFIER_ID': '28987', 'IDENTIFIER_TYPE': 'gene', 'SCORE.3': '-', 'SCORE.2': '0.999965', 'SCORE.4': '-', 'SCORE.5': '-', 'SCORE.1': '0.96316', 'HIT': 'NO', 'SOURCE': 'BioGRID ORCS', 'SCREEN_ID': '178', 'ORGANISM_ID': '9606', 'OFFICIAL_SYMBOL': 'NOB1', 'ALIASES': 'ART-4|MST158|MSTP158|NOB1P|PSMD8BP1', 'ORGANISM_OFFICIAL': 'Homo sapiens'}
"""  # noqa: E501
