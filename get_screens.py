#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch screen annotation with customizable search criteria
that can be tailored to match your own requirements
"""

import requests
from core import config as cfg

request_url = cfg.BASE_URL + "/screens/"

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this instance, we've limited the results to only those in the cellLine hela and with the
# library methodology of "knockout"
params = {
    "accesskey": cfg.ACCESS_KEY,
    "cellLine": "hela",
    "libraryMethodology": "knockout",
    "format": "json"
}

r = requests.get( request_url, params = params )
screens = r.json( )

for screen in screens :
    print( screen )

"""
Output as of version 1.0.1
{'CONDITION_DOSAGE': '-', 'CELL_LINE': 'HeLa', 'SIGNIFICANCE_CRITERIA': 'Score.1 (Bayes Factor) > 15.47', 'DURATION': '18 Days', 'SCORE_COL_COUNT': '1', 'SCREEN_NAME': '2-PMID26627737', 'SOURCE_ID': '26627737', 'SCORE.4_TYPE': '-', 'FULL_SIZE_AVAILABLE': 'Yes', 'ANALYSIS': 'BAGEL', 'SOURCE_TYPE': 'pubmed', 'CONDITION_NAME': '-', 'ORGANISM_ID': '9606', 'EXPERIMENTAL_SETUP': 'Timecourse', 'SCREEN_ID': '17', 'METHODOLOGY': 'Knockout', 'SCORE.2_TYPE': '-', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.1_TYPE': 'Bayes Factor', 'AUTHOR': 'Hart T (2015)', 'SOURCE': 'BioGRID ORCS', 'NOTES': 'Genes with a Bayes Factor (BF) above the threshold of 15.47 at an FDR of 5% (FDR < 0.05) were identified as fitness genes (hits) for this cell line in this CRISPR screen.', 'SCREEN_FORMAT': 'Pool', 'THROUGHPUT': 'High Throughput', 'SIGNIFICANCE_INDICATOR': 'Score Significance', 'CELL_TYPE': 'Cervical Adenocarcinoma Cell Line', 'PHENOTYPE': 'viability', 'SCORE.3_TYPE': '-', 'ENZYME': 'CAS9', 'MOI': '~ 0.3', 'NUMBER_OF_HITS': '1696', 'LIBRARY_TYPE': 'CRISPRn', 'FULL_SIZE': '17661', 'SCORE.5_TYPE': '-', 'SCORES_SIZE': '17648', 'SCREEN_TYPE': 'Negative Selection', 'LIBRARY': 'TKO (Toronto Knockout) v1'}
{'CONDITION_DOSAGE': '100 nM', 'CELL_LINE': 'HeLa', 'SIGNIFICANCE_CRITERIA': '-', 'DURATION': '3 Hours', 'SCORE_COL_COUNT': '2', 'SCREEN_NAME': '1-PMID28894007', 'SOURCE_ID': '28894007', 'SCORE.4_TYPE': '-', 'FULL_SIZE_AVAILABLE': 'Yes', 'ANALYSIS': 'MaGeCK', 'SOURCE_TYPE': 'pubmed', 'CONDITION_NAME': 'Insulin', 'ORGANISM_ID': '9606', 'EXPERIMENTAL_SETUP': 'Ligand Exposure', 'SCREEN_ID': '178', 'METHODOLOGY': 'Knockout', 'SCORE.2_TYPE': 'FDR', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.1_TYPE': 'p-Value', 'AUTHOR': 'Gulbranson DR (2017)', 'SOURCE': 'BioGRID ORCS', 'NOTES': 'Authors screened cells for exocytosis defects. Hela cells expressing tagged GLUT4 were exposed to insulin and then FACs sorted to identify cells with reduced surface expression of Glut4.', 'SCREEN_FORMAT': 'Pool', 'THROUGHPUT': 'High Throughput', 'SIGNIFICANCE_INDICATOR': 'Column Significance', 'CELL_TYPE': 'Cervical Adenocarcinoma Cell Line', 'PHENOTYPE': 'protein transport', 'SCORE.3_TYPE': '-', 'ENZYME': 'CAS9', 'MOI': '~ 0.4', 'NUMBER_OF_HITS': '329', 'LIBRARY_TYPE': 'CRISPRn', 'FULL_SIZE': '18737', 'SCORE.5_TYPE': '-', 'SCORES_SIZE': '18737', 'SCREEN_TYPE': 'Phenotype Screen', 'LIBRARY': 'GECKO v2'}
{'CONDITION_DOSAGE': '-', 'CELL_LINE': 'HeLa', 'SIGNIFICANCE_CRITERIA': 'Score.1 (Log10 (p-value)) > 1.3', 'DURATION': '21 Days', 'SCORE_COL_COUNT': '1', 'SCREEN_NAME': '1-PMID28775154', 'SOURCE_ID': '28775154', 'SCORE.4_TYPE': '-', 'FULL_SIZE_AVAILABLE': 'Yes', 'ANALYSIS': 'RSA', 'SOURCE_TYPE': 'pubmed', 'CONDITION_NAME': '-', 'ORGANISM_ID': '9606', 'EXPERIMENTAL_SETUP': 'Timecourse', 'SCREEN_ID': '405', 'METHODOLOGY': 'Knockout', 'SCORE.2_TYPE': '-', 'ORGANISM_OFFICIAL': 'Homo sapiens', 'SCORE.1_TYPE': 'Log10 (p-value)', 'AUTHOR': 'Stewart SE (2017)', 'SOURCE': 'BioGRID ORCS', 'NOTES': 'Authors screened for genes  required for cell surface localization of Gal-3.', 'SCREEN_FORMAT': 'Pool', 'THROUGHPUT': 'High Throughput', 'SIGNIFICANCE_INDICATOR': 'Score Significance', 'CELL_TYPE': 'Cervical Adenocarcinoma Cell Line', 'PHENOTYPE': 'protein/peptide accumulation', 'SCORE.3_TYPE': '-', 'ENZYME': 'CAS9', 'MOI': '~ 0.2', 'NUMBER_OF_HITS': '1174', 'LIBRARY_TYPE': 'CRISPRn', 'FULL_SIZE': '20916', 'SCORE.5_TYPE': '-', 'SCORES_SIZE': '20916', 'SCREEN_TYPE': 'Phenotype Screen', 'LIBRARY': 'GECKO v2'}
"""