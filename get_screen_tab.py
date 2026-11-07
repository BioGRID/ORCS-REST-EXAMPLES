#!/usr/bin/env python3

"""
Fetch screen scores with customizable search criteria
that can be tailored to match your own requirements
in tab format
"""

import httpx
from loguru import logger

from core import config as cfg


def main() -> None:
    screen_id = 178
    request_url = f"{cfg.BASE_URL}/screen/{screen_id}"

    # These parameters can be modified to match any search criteria following
    # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
    # In this instance, we've chosen to return results in "tab" format with a header, and
    # to limit scores in the SCORE.1 column to the range of 0.9 -> 0.98
    params = {
        "accesskey": cfg.ACCESS_KEY,
        "format": "tab",
        "header": "yes",
        "score1min": 0.9,
        "score1max": 0.98,
    }

    response = httpx.get(request_url, params=params, timeout=30)
    response.raise_for_status()
    lines = response.text.splitlines()

    # The first line is the header, so we skip it with lines[1:].
    # You could also turn the header off with "header": "no" as a parameter instead.
    data = {}
    for line in lines[1:]:
        # Tab files are tab delimited
        row = line.split("\t")

        # Create a lookup of results by gene identifier (the second column)
        data[row[1]] = row

    # Print out data about the genes BRIX1, ASB4, and NOB1
    for gene_id in ["55299", "51666", "28987"]:
        logger.info("Gene {}: {}", gene_id, data[gene_id])


if __name__ == "__main__":
    main()

"""
Output as of version 1.0.1:
['178', '55299', 'gene', 'BRIX1', 'BRIX|BXDC2|FLJ11100', '9606', 'Homo sapiens', '0.94239', '0.999965', '-', '-', '-', 'NO', 'BioGRID ORCS']
['178', '51666', 'gene', 'ASB4', 'ASB-4', '9606', 'Homo sapiens', '0.97613', '0.999965', '-', '-', '-', 'NO', 'BioGRID ORCS']
['178', '28987', 'gene', 'NOB1', 'ART-4|MST158|MSTP158|NOB1P|PSMD8BP1', '9606', 'Homo sapiens', '0.96316', '0.999965', '-', '-', '-', 'NO', 'BioGRID ORCS']
"""  # noqa: E501
