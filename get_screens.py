#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fetch screen annotation with customizable search criteria
that can be tailored to match your own requirements
"""

import requests
import json
from core import config as cfg

request_url = cfg.BASE_URL + "/screens/"
params = {
    "accesskey": cfg.ACCESS_KEY,
    "cellLine": "hela",
    "libraryMethodology": "knockout",
    "format": "json"
}

r = requests.get( request_url, params = params )
print( r.url )

print( r.text )