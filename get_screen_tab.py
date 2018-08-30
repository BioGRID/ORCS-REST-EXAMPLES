#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch screen scores with customizable search criteria
that can be tailored to match your own requirements
in tab format
"""

import requests
from core import config as cfg

screen_id = 178
request_url = cfg.BASE_URL + "/screen/" + str(screen_id)

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this instance, we've chosen to return results in "tab" format with a header, and 
# to limit scores in the SCORE.1 column to the range of 0.9 -> 0.98
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "tab",
    "header": "yes",
    "score1min": 0.9,
    "score1max": 0.98
}

r = requests.get( request_url, params = params )
screen = r.text.splitlines( )

row_count = 0
data = {}
for row in screen :

    # Skip the header, but you could have also simply turned
    # it off with header: "no" as a parameter instead
    if row_count == 0 :
        row_count = row_count + 1
        continue

    # Tab files are tab delimited
    row = row.split( "\t" )
    
    # create a hash of results by gene identifier
    data[row[1]] = row

# Print out data about the genes BRIX1, ASB4, and NOB1
print( data['55299'] )
print( data['51666'] )
print( data['28987'] )

""" 
Output as of version 1.0.1:
['178', '55299', 'gene', 'BRIX1', 'BRIX|BXDC2|FLJ11100', '9606', 'Homo sapiens', '0.94239', '0.999965', '-', '-', '-', 'NO', 'BioGRID ORCS']
['178', '51666', 'gene', 'ASB4', 'ASB-4', '9606', 'Homo sapiens', '0.97613', '0.999965', '-', '-', '-', 'NO', 'BioGRID ORCS']
['178', '28987', 'gene', 'NOB1', 'ART-4|MST158|MSTP158|NOB1P|PSMD8BP1', '9606', 'Homo sapiens', '0.96316', '0.999965', '-', '-', '-', 'NO', 'BioGRID ORCS']
"""