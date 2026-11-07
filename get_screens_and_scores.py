#!/usr/bin/env python3

"""
Fetch screen annotation with customizable search criteria
that can be tailored to match your own requirements. Then fetch
the score values associated with those screens.
"""

import httpx
from loguru import logger

from core import config as cfg


def main() -> None:
    # This example makes one request per screen, so we use a single httpx.Client.
    # The client reuses the same connection for every request, which is much faster
    # than opening a new connection each time.
    with httpx.Client(timeout=30) as client:
        request_url = f"{cfg.BASE_URL}/screens/"

        # These parameters can be modified to match any search criteria following
        # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
        # In this example, we've chosen to only receive toxin exposure and virus exposure
        # experiments and also to limit to only human results.
        params = {
            "accesskey": cfg.ACCESS_KEY,
            "experimentalSetup": "toxin exposure|virus exposure",
            "organismID": "9606",
            "format": "json",
        }

        response = client.get(request_url, params=params)
        response.raise_for_status()
        screens = response.json()
        logger.info("Number of Screens Found: {}", len(screens))

        # Step through each matching screen, and make a request
        # for the associated score data
        scores = {}
        for screen in screens:
            screen_id = str(screen["SCREEN_ID"])
            request_url = f"{cfg.BASE_URL}/screen/{screen_id}"

            # These parameters can be modified to match any search criteria following
            # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
            # if you are not interested in a full set of score data. In this case, we only want
            # scores marked as hits.
            params = {
                "accesskey": cfg.ACCESS_KEY,
                "format": "json",
                "hit": "yes",
            }

            response = client.get(request_url, params=params)
            response.raise_for_status()
            score_set = response.json()

            # Convert the returned score_set into an indexed one
            # where you can retrieve rows by IDENTIFIER_ID
            indexed_scores = {}
            for row in score_set:
                indexed_scores[row["IDENTIFIER_ID"]] = row

            scores[screen_id] = indexed_scores

    # Print results for the same gene (TFAP4, 7023) from each screen
    # if it's in the associated list of hits
    gene_id = "7023"
    for screen_id, score_set in scores.items():
        if gene_id in score_set:
            logger.info("Gene {} is a hit in screen {}: {}", gene_id, screen_id, score_set[gene_id])

    logger.info("Number of Score Sets: {}", len(scores))


if __name__ == "__main__":
    main()

"""
Output as of version 1.0.1
Number of Screens Found: 10
{'IDENTIFIER_ID': '7023', 'SCORE.4': '0', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '169', 'SCORE.2': '0', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '8.732195741', 'HIT': 'YES', 'SCORE.3': '0', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
{'IDENTIFIER_ID': '7023', 'SCORE.4': '-', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '24', 'SCORE.2': '1.9', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '19.7', 'HIT': 'YES', 'SCORE.3': '0.00285', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
{'IDENTIFIER_ID': '7023', 'SCORE.4': '0.960101193', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '170', 'SCORE.2': '0.831183816', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '1.384515796', 'HIT': 'YES', 'SCORE.3': '0.963569948', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
{'IDENTIFIER_ID': '7023', 'SCORE.4': '0', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '168', 'SCORE.2': '0', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '12.38037506', 'HIT': 'YES', 'SCORE.3': '0', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
Number of Score Sets: 10
"""  # noqa: E501
