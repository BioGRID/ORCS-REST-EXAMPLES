#!/usr/bin/env python3

"""
Fetch scores across all screens for a single gene
using customizable filtering options
"""

import httpx
from loguru import logger

from core import config as cfg


def main() -> None:
    gene_id = 7023
    request_url = f"{cfg.BASE_URL}/gene/{gene_id}"

    # These parameters can be modified to match any search criteria following
    # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
    # In this particular instance, we've chosen to limit results to only those in which
    # our gene of interest is considered a hit
    params = {
        "accesskey": cfg.ACCESS_KEY,
        "format": "json",
        "hit": "yes",
    }

    response = httpx.get(request_url, params=params, timeout=30)
    response.raise_for_status()
    scores = response.json()

    # Create a lookup of results by screen identifier
    data = {}
    for row in scores:
        data[row["SCREEN_ID"]] = row

    # Print out data about the gene from several specific screens
    for screen_id in ["549", "170", "197"]:
        logger.info("Gene {} in screen {}: {}", gene_id, screen_id, data[screen_id])


if __name__ == "__main__":
    main()

"""
Output as of version 1.0.1:
{'SCORE.2': '0.0108', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'IDENTIFIER_TYPE': 'gene', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.3': '-', 'SCREEN_ID': '549', 'HIT': 'YES', 'IDENTIFIER_ID': '7023', 'SCORE.1': '-0.6694077', 'SOURCE': 'BioGRID ORCS', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606', 'SCORE.4': '-', 'SCORE.5': '-'}
{'SCORE.2': '0.831183816', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'IDENTIFIER_TYPE': 'gene', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.3': '0.963569948', 'SCREEN_ID': '170', 'HIT': 'YES', 'IDENTIFIER_ID': '7023', 'SCORE.1': '1.384515796', 'SOURCE': 'BioGRID ORCS', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606', 'SCORE.4': '0.960101193', 'SCORE.5': '-'}
{'SCORE.2': '0.00408', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'IDENTIFIER_TYPE': 'gene', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.3': '-', 'SCREEN_ID': '197', 'HIT': 'YES', 'IDENTIFIER_ID': '7023', 'SCORE.1': '-0.595238539', 'SOURCE': 'BioGRID ORCS', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606', 'SCORE.4': '-', 'SCORE.5': '-'}
"""  # noqa: E501
