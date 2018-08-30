#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch screen scores with customizable search criteria
that can be tailored to match your own requirements
in json format
"""

import requests
from core import config as cfg

screen_id = 178
request_url = cfg.BASE_URL + "/screen/" + str(screen_id)
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json",
    "score1min": 0.9,
    "score1max": 0.98
}

r = requests.get( request_url, params = params )
screen = r.json( )

data = {}
for row in screen :
    # create a hash of results by gene identifier
    data[row['IDENTIFIER_ID']] = row

# Print out data about the genes BRIX1, ASB4, and NOB1
print( data['55299'] )
print( data['51666'] )
print( data['28987'] )

""" 
Output as of version 1.0.1:
{'IDENTIFIER_ID': '55299', 'IDENTIFIER_TYPE': 'gene', 'SCORE.3': '-', 'SCORE.2': '0.999965', 'SCORE.4': '-', 'SCORE.5': '-', 'SCORE.1': '0.94239', 'HIT': 'NO', 'SOURCE': 'BioGRID ORCS', 'SCREEN_ID': '178', 'ORGANISM_ID': '9606', 'OFFICIAL_SYMBOL': 'BRIX1', 'ALIASES': 'BRIX|BXDC2|FLJ11100', 'ORGANISM_OFFICIAL': 'Homo sapiens'}
{'IDENTIFIER_ID': '51666', 'IDENTIFIER_TYPE': 'gene', 'SCORE.3': '-', 'SCORE.2': '0.999965', 'SCORE.4': '-', 'SCORE.5': '-', 'SCORE.1': '0.97613', 'HIT': 'NO', 'SOURCE': 'BioGRID ORCS', 'SCREEN_ID': '178', 'ORGANISM_ID': '9606', 'OFFICIAL_SYMBOL': 'ASB4', 'ALIASES': 'ASB-4', 'ORGANISM_OFFICIAL': 'Homo sapiens'}
{'IDENTIFIER_ID': '28987', 'IDENTIFIER_TYPE': 'gene', 'SCORE.3': '-', 'SCORE.2': '0.999965', 'SCORE.4': '-', 'SCORE.5': '-', 'SCORE.1': '0.96316', 'HIT': 'NO', 'SOURCE': 'BioGRID ORCS', 'SCREEN_ID': '178', 'ORGANISM_ID': '9606', 'OFFICIAL_SYMBOL': 'NOB1', 'ALIASES': 'ART-4|MST158|MSTP158|NOB1P|PSMD8BP1', 'ORGANISM_OFFICIAL': 'Homo sapiens'}
"""