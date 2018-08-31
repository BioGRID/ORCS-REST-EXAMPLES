#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch the set of controlled vocabularies and also fetch
a set of terms for two of the vocabulary categories
"""

import requests
from core import config as cfg

request_url = cfg.BASE_URL + "/vocabs"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this particular instance, we've chosen just the format to use in json
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json"
}

r = requests.get( request_url, params = params )
vocabs = r.json( )

print( vocabs )

""" 
Output as of version 1.0.1:
{'8': 'Screen Format', '4': 'Condition Name', '10': 'Cell Line', '12': 'Phenotype', '3': 'Experimental Setup', '2': 'Screen Type', '1': 'Throughput', '9': 'Enzyme', '6': 'Library Type', '11': 'Cell Type', '5': 'Library', '7': 'Library Methodology', '15': 'Statistical Analysis'}
""" 

# Now we can request the actual terms in these controlled vocabularies
request_url = cfg.BASE_URL + "/vocab/"
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json"
}

# Fetch list of available phenotypes (vocab: 12)
r = requests.get( request_url + '12', params = params )
vocab = r.json( )

print( vocab )

"""
Output as of version 1.0.1:
{'51': 'resistance to chemicals', '314': 'protein transport', '261': 'cell cycle progression', '53': 'resistance to virus', '50': 'viability', '141': 'toxin resistance', '309': 'regulation of signal transduction phenotype', '325': 'protein/peptide accumulation'}
"""

# Fetch list of available enzymes (vocab: 9)
r = requests.get( request_url + '9', params = params )
vocab = r.json( )

print( vocab )

"""
Output as of version 1.0.1:
{'36': 'sam (nls-dcas9-vp64/ms2-p65-hsf1)', '35': 'cas9', '38': 'suncas9', '37': 'dcas9-krab'}
"""