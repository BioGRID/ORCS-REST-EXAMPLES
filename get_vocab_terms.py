#!/usr/bin/env python3

"""
Fetch the set of controlled vocabularies and also fetch
a set of terms for two of the vocabulary categories
"""

import httpx
from loguru import logger

from core import config as cfg


def main() -> None:
    # This example makes several requests, so we use a single httpx.Client.
    # The client reuses the same connection for every request, which is faster
    # than opening a new connection each time.
    with httpx.Client(timeout=30) as client:
        request_url = f"{cfg.BASE_URL}/vocabs"

        # These parameters can be modified to match any search criteria following
        # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
        # In this particular instance, we've chosen just the format to use in json
        params = {
            "accesskey": cfg.ACCESS_KEY,
            "format": "json",
        }

        response = client.get(request_url, params=params)
        response.raise_for_status()
        vocabs = response.json()

        logger.info("Vocabularies: {}", vocabs)

        """
        Output as of version 1.0.1:
        {'8': 'Screen Format', '4': 'Condition Name', '10': 'Cell Line', '12': 'Phenotype', '3': 'Experimental Setup', '2': 'Screen Type', '1': 'Throughput', '9': 'Enzyme', '6': 'Library Type', '11': 'Cell Type', '5': 'Library', '7': 'Library Methodology', '15': 'Statistical Analysis'}
        """  # noqa: E501

        # Now we can request the actual terms in these controlled vocabularies

        # Fetch list of available phenotypes (vocab: 12)
        response = client.get(f"{cfg.BASE_URL}/vocab/12", params=params)
        response.raise_for_status()
        phenotypes = response.json()

        logger.info("Phenotype terms: {}", phenotypes)

        """
        Output as of version 1.0.1:
        {'51': 'resistance to chemicals', '314': 'protein transport', '261': 'cell cycle progression', '53': 'resistance to virus', '50': 'viability', '141': 'toxin resistance', '309': 'regulation of signal transduction phenotype', '325': 'protein/peptide accumulation'}
        """  # noqa: E501

        # Fetch list of available enzymes (vocab: 9)
        response = client.get(f"{cfg.BASE_URL}/vocab/9", params=params)
        response.raise_for_status()
        enzymes = response.json()

        logger.info("Enzyme terms: {}", enzymes)

        """
        Output as of version 1.0.1:
        {'36': 'sam (nls-dcas9-vp64/ms2-p65-hsf1)', '35': 'cas9', '38': 'suncas9', '37': 'dcas9-krab'}
        """  # noqa: E501


if __name__ == "__main__":
    main()
