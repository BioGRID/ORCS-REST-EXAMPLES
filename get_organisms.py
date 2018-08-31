#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch the set of currently supported organism IDs
"""

import requests
from core import config as cfg

request_url = cfg.BASE_URL + "/organisms"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this particular instance, we've chosen just the format to use in json
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json"
}

r = requests.get( request_url, params = params )
organisms = r.json( )

print( organisms )

""" 
Output as of version 1.0.1:
{'10090': 'Mus musculus', '9606': 'Homo sapiens'}
""" 