#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch genes with customizable search criteria
that can be tailored to match your own requirements. Then fetch 
the screen annotation associated with those gene scores.
"""

import requests
from core import config as cfg

request_url = cfg.BASE_URL + "/genes/"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this example, we've chosen to only receive scores for the genes DPF2, SULT1E1, UBQLN4
# and also to limit to only human results. Also, we only want scores considered to be significant
# hits.
params = {
    "accesskey": cfg.ACCESS_KEY,
    "name": "DPF2|SULT1E1|UBQLN4",
    "organismID": "9606",
    "hit": "yes",
    "format": "json"
}

r = requests.get( request_url, params = params )
scores = r.json( )
print( "Number of Scores Found: " + str(len(scores)) )

# Step through all the scores and build a unique set of screens
# as well as build a two dimentional structure for storing results
# where the identifier ID is the outer level and the screen ID is the
# inner level. This will allow us to lookup genes and then screens for that
# gene later on.
screen_ids = set( )
genes = {}
for score in scores :
    screen_ids.add( score['SCREEN_ID'] )
    
    if score['IDENTIFIER_ID'] not in genes :
        genes[score['IDENTIFIER_ID']] = {}

    genes[score['IDENTIFIER_ID']][score['SCREEN_ID']] = score

print( "Number of Unique Screen IDs Found: " + str(len(screen_ids)) )
print( "Number of Genes Found: " + str(len(genes)) )

# Make a new request for annotation about all the new screens
request_url = cfg.BASE_URL + "/screens/"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this example, we are passing in a list of actual screen IDs we want
params = {
    "accesskey": cfg.ACCESS_KEY,
    "screenID": "|".join( screen_ids ),
    "format": "json"
}

r = requests.get( request_url, params = params )
screens = r.json( )
print( "Number of Screen Details Retrieved: " + str(len(screens)) )

# Step through each screen and build a nice index of screens by screen_id
screen_lookup = {}
for screen in screens :
    screen_lookup[screen['SCREEN_ID']] = screen

# Print out a score and its associated screen annotation
# for gene 5977 and screen 201
print( genes['5977']['201'] )
print( screen_lookup['201'] )

"""
Output as of version 1.0.1
Number of Scores Found: 311
Number of Unique Screen IDs Found: 235
Number of Genes Found: 3
Number of Screen Details Retrieved: 235
{'ALIASES': 'REQ|UBID4|ubi-d4|BAF45d', 'SCORE.1': '-0.492155932', 'SCORE.4': '-', 'SOURCE': 'BioGRID ORCS', 'ORGANISM_ID': '9606', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.2': '0.028', 'SCREEN_ID': '201', 'HIT': 'YES', 'IDENTIFIER_ID': '5977', 'SCORE.3': '-', 'IDENTIFIER_TYPE': 'gene', 'OFFICIAL_SYMBOL': 'DPF2', 'SCORE.5': '-'}
{'SOURCE_ID': '29083409', 'THROUGHPUT': 'High Throughput', 'PHENOTYPE': 'viability', 'SCORE.3_TYPE': '-', 'ORGANISM_ID': '9606', 'SCREEN_TYPE': 'Negative Selection', 'FULL_SIZE_AVAILABLE': 'Yes', 'DURATION': '21 Days', 'CELL_TYPE': 'glioma cell line', 'SCREEN_NAME': '21-PMID29083409', 'CELL_LINE': 'U-343 MG-A cell', 'SIGNIFICANCE_INDICATOR': 'Score Significance', 'SCORE.1_TYPE': 'CERES score', 'CONDITION_DOSAGE': '-', 'SCORE.5_TYPE': '-', 'SCORES_SIZE': '17670', 'NOTES': 'To identify gene hits at an FDR < 0.05, ORCS estimated FDRs for the CERES Avana dataset using customized gold-standard positive and negative sets of genes. The custom positive set included genes essential in at least 90% of cell lines in both the CERES Avana dataset (PMID:29083409) and the 10 lines included in Bertomeu et al. (PMID:29038160). The custom negative set included genes essential in zero cell lines from one of the two datasets and in <=10% of the other dataset.', 'ANALYSIS': 'CERES', 'AUTHOR': 'Meyers RM (2017)', 'SOURCE_TYPE': 'pubmed', 'SCORE.2_TYPE': 'FDR', 'LIBRARY_TYPE': 'CRISPRn', 'SOURCE': 'BioGRID ORCS', 'MOI': '< 1', 'SCREEN_ID': '201', 'LIBRARY': 'Avana', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SIGNIFICANCE_CRITERIA': 'Score.2 (FDR) < 0.05', 'ENZYME': 'CAS9', 'NUMBER_OF_HITS': '1948', 'CONDITION_NAME': '-', 'SCORE_COL_COUNT': '2', 'METHODOLOGY': 'Knockout', 'SCREEN_FORMAT': 'Pool', 'FULL_SIZE': '17670', 'EXPERIMENTAL_SETUP': 'Timecourse', 'SCORE.4_TYPE': '-'}
"""