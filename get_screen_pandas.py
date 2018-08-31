#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch screen scores in json format, and load the results
into a pandas dataframe. Pandas is a convenient library for
loading tabular datasets and provides the ability to perform
subsequent queries on the loaded dataframe after tbe fact.
"""

import requests
import pandas as pd
from core import config as cfg

screen_id = 205
request_url = cfg.BASE_URL + "/screen/" + str(screen_id)

# These parameters can be modified to match any search criteria following
# the rules outlined in the Wiki: https://wiki.thebiogrid.org/doku.php/orcs:webservice
# In this particular case, we've chosen to return everything in the json format.
params = {
    "accesskey": cfg.ACCESS_KEY,
    "format": "json"
}

r = requests.get( request_url, params = params )
screen = r.json( )

data = {}
for row in screen :
    # create a hash of results by gene identifier
    data[row['IDENTIFIER_ID']] = row

# Load dataset into pandas dataframe
dataset = pd.DataFrame.from_dict( data, orient='index' )

# Re-order the columns to remove the un-needed columns
columns = ['IDENTIFIER_TYPE', 'OFFICIAL_SYMBOL', 'ALIASES', 'ORGANISM_ID', 'ORGANISM_OFFICIAL', 'SCORE.1', 'SCORE.2', 'HIT', 'SOURCE']
dataset = dataset[columns]

# Convert numeric columns into floats
dataset[['SCORE.1','SCORE.2']] = dataset[['SCORE.1','SCORE.2']].apply( pd.to_numeric )

# Print all rows with SCORE.1 > 1
print( dataset.loc[dataset['SCORE.1'] > 1] )

""" 
Output as of version 1.0.1:
          IDENTIFIER_TYPE OFFICIAL_SYMBOL                              ALIASES ORGANISM_ID ORGANISM_OFFICIAL   SCORE.1  SCORE.2 HIT        SOURCE
100302736            gene    TMED7-TICAM2                                    -        9606      Homo sapiens  1.007427    0.382  NO  BioGRID ORCS
11235                gene          PDCD10                          CCM3|TFAR15        9606      Homo sapiens  1.007427    0.382  NO  BioGRID ORCS
154791               gene            FMC1                      C7orf55|HSPC268        9606      Homo sapiens  1.138414    0.382  NO  BioGRID ORCS
729873               gene          TBC1D3  PRC17|TBC1D3A|TBC1D3F|DKFZp434P2235        9606      Homo sapiens  2.968792    0.382  NO  BioGRID ORCS
"""

# Print hits only
print( dataset.loc[dataset['HIT'] == 'YES'])

""" 
Output as of version 1.0.1:
         IDENTIFIER_TYPE OFFICIAL_SYMBOL                                            ALIASES ORGANISM_ID ORGANISM_OFFICIAL   SCORE.1  SCORE.2  HIT        SOURCE
10001                gene            MED6                                    ARC33|NY-REN-28        9606      Homo sapiens -0.779074  0.00721  YES  BioGRID ORCS
100049587            gene        SIGLEC14                                                  -        9606      Homo sapiens -0.545794  0.02040  YES  BioGRID ORCS
100287932            gene          TIMM23                                              TIM23        9606      Homo sapiens -0.587844  0.01160  YES  BioGRID ORCS
10036                gene          CHAF1A                     CAF-1|CAF1|CAF1B|CAF1P150|P150        9606      Homo sapiens -1.175897  0.00000  YES  BioGRID ORCS
100462977            gene        MTRNR2L1                                                HN1        9606      Homo sapiens -0.493905  0.03430  YES  BioGRID ORCS
100463486            gene        MTRNR2L8                                                HN8        9606      Homo sapiens -0.528771  0.02220  YES  BioGRID ORCS
10051                gene            SMC4                     CAP-C|CAPC|SMC-4|SMC4L1|hCAP-C        9606      Homo sapiens -0.843711  0.00269  YES  BioGRID ORCS
100526842            gene  RPL17-C18orf32                                                  -        9606      Homo sapiens -0.480266  0.04050  YES  BioGRID ORCS
...                   ...             ...                                                ...         ...               ...       ...      ...  ...           ...
"""