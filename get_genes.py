#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch scores for several genes across the entire set
of screens in the database
"""

import requests
from core import config as cfg

request_url = cfg.BASE_URL + "/genes/"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this instance, we've limited the results to the entrez gene identifiers 66050|66056|66044
params = {
    "accesskey": cfg.ACCESS_KEY,
    "geneID": '66050|66056|66044',
    "format": "json"
}

r = requests.get( request_url, params = params )
scores = r.json( )

for score in scores :
    print( score )

"""
Output as of version 1.0.1
{'SCORE.2': '1', 'OFFICIAL_SYMBOL': '0610009B22Rik', 'HIT': 'NO', 'IDENTIFIER_ID': '66050', 'ORGANISM_OFFICIAL': 'Mus musculus', 'ORGANISM_ID': '10090', 'SCORE.5': '-', 'SCORE.1': '0.71157', 'SCORE.3': '-', 'IDENTIFIER_TYPE': 'gene', 'SOURCE': 'BioGRID ORCS', 'ALIASES': '-', 'SCREEN_ID': '578', 'SCORE.4': '-'}
{'SCORE.2': '1', 'OFFICIAL_SYMBOL': 'Dtd1', 'HIT': 'NO', 'IDENTIFIER_ID': '66044', 'ORGANISM_OFFICIAL': 'Mus musculus', 'ORGANISM_ID': '10090', 'SCORE.5': '-', 'SCORE.1': '0.6958', 'SCORE.3': '-1.4566', 'IDENTIFIER_TYPE': 'gene', 'SOURCE': 'BioGRID ORCS', 'ALIASES': '0610006H08Rik|DUE-B|Hars2', 'SCREEN_ID': '165', 'SCORE.4': '-'}
{'SCORE.2': '1', 'OFFICIAL_SYMBOL': 'Zfp524', 'HIT': 'NO', 'IDENTIFIER_ID': '66056', 'ORGANISM_OFFICIAL': 'Mus musculus', 'ORGANISM_ID': '10090', 'SCORE.5': '-', 'SCORE.1': '0.96692', 'SCORE.3': '-0.48795', 'IDENTIFIER_TYPE': 'gene', 'SOURCE': 'BioGRID ORCS', 'ALIASES': '0610012F07Rik|2300009P13Rik|Znf524', 'SCREEN_ID': '163', 'SCORE.4': '-'}
"""