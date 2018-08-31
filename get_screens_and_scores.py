#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch screen annotation with customizable search criteria
that can be tailored to match your own requirements. Then fetch 
the score values associated with those screens.
"""

import requests
from core import config as cfg

request_url = cfg.BASE_URL + "/screens/"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this example, we've chosen to only receive toxin exposure and virus exposure experiments
# and also to limit to only human results.
params = {
    "accesskey": cfg.ACCESS_KEY,
    "experimentalSetup": "toxin exposure|virus exposure",
    "organismID": "9606",
    "format": "json"
}

r = requests.get( request_url, params = params )
screens = r.json( )
print( "Number of Screens Found: " + str(len(screens)) )

# Step through each matching screen, and make a request
# for the associated score data
scores = {}
for screen in screens :
    request_url = cfg.BASE_URL + "/screen/" + str(screen['SCREEN_ID'])

    # These parameters can be modified to match any search criteria following
    # the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
    # if you are not interested in a full set of score data. In this case, we only want scores
    # marked as hits.
    params = {
        "accesskey": cfg.ACCESS_KEY,
        "format": "json",
        "hit": "yes"
    }

    r = requests.get( request_url, params = params )
    score_set = r.json( )

    # Convert the returned score_set into an indexed one 
    # where you can retrieve rows by IDENTIFIER_ID
    indexed_scores = {}
    for row in score_set :
        indexed_scores[row['IDENTIFIER_ID']] = row

    scores[str(screen['SCREEN_ID'])] = indexed_scores

# Print Results for the same gene (AACS) from each screen
# If it's in the associated list of hits
for screen_id, score_set in scores.items( ) :
    if '7023' in score_set :
        print( score_set['7023'] )

print( "Number of Score Sets: " + str(len(scores)) )

"""
Output as of version 1.0.1
Number of Screens Found: 10
{'IDENTIFIER_ID': '7023', 'SCORE.4': '0', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '169', 'SCORE.2': '0', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '8.732195741', 'HIT': 'YES', 'SCORE.3': '0', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
{'IDENTIFIER_ID': '7023', 'SCORE.4': '-', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '24', 'SCORE.2': '1.9', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '19.7', 'HIT': 'YES', 'SCORE.3': '0.00285', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
{'IDENTIFIER_ID': '7023', 'SCORE.4': '0.960101193', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '170', 'SCORE.2': '0.831183816', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '1.384515796', 'HIT': 'YES', 'SCORE.3': '0.963569948', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
{'IDENTIFIER_ID': '7023', 'SCORE.4': '0', 'SOURCE': 'BioGRID ORCS', 'IDENTIFIER_TYPE': 'gene', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.5': '-', 'SCREEN_ID': '168', 'SCORE.2': '0', 'OFFICIAL_SYMBOL': 'TFAP4', 'SCORE.1': '12.38037506', 'HIT': 'YES', 'SCORE.3': '0', 'ALIASES': 'AP-4|bHLHc41', 'ORGANISM_ID': '9606'}
Number of Score Sets: 10
"""