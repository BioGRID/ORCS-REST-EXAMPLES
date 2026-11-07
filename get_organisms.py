#!/usr/bin/env python3

"""
Fetch the set of currently supported organism IDs
"""

import httpx
from loguru import logger

from core import config as cfg


def main() -> None:
    request_url = f"{cfg.BASE_URL}/organisms"

    # These parameters can be modified to match any search criteria following
    # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
    # In this particular instance, we've chosen just the format to use in json
    params = {
        "accesskey": cfg.ACCESS_KEY,
        "format": "json",
    }

    response = httpx.get(request_url, params=params, timeout=30)
    response.raise_for_status()
    organisms = response.json()

    logger.info("Supported organisms: {}", organisms)


if __name__ == "__main__":
    main()

"""
Output as of version 1.0.1:
{'10090': 'Mus musculus', '9606': 'Homo sapiens'}
"""
