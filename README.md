# BioGRID ORCS Web Service Examples
Sample code for accessing the BioGRID ORCS Rest Service and working with the resulting datasets.

## Development Status
+ **Status**: In Progress

## Requirements
+ Python 3.6.5+
+ Required Python libraries are listed in requirements.txt. To install them all simply run the following from within your development environment: 
  + **pip3 install -r requirements.txt**
+ We also recommend installing virtualenv and virtualenvwrapper for a containerized python environment ([**Setup Instructions**](https://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu/244642#244642)) but this is optional.

## Configuration
+ All configuration options are located in the config/config.sample.yml file in YAML format. Simply rename the file to config.yml and update the options contained within to reflect your own environment.
+ All access to the BioGRID ORCS Webservice requires an individual access key. It's free to signup to use it. You will need to register at **https://orcsws.thebiogrid.org/** to obtain one, and enter it in your config file for it to be accessible from all example code in this repository.
+ For a listing of all configurable search parameters when making requests, visit our wiki: **https://wiki.thebiogrid.org/doku.php/orcs:webservice**

## How to Run
+ After completing the configuration steps above. Simply run: **python3 \<script name\>** at the command prompt. Example: **python3 get_screen_tab.py**

## Examples
+ [**get_organisms.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_organisms.py) - Obtain currently supported organism ids
+ [**get_vocab_terms.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_vocab_terms.py) - Obtain controlled vocabulary terms to help you create requests for other endpoints of the API
+ [**get_screen_tab.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_tab.py) - Obtain score information for a single screen in tab format
+ [**get_screen_json.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_json.py) - Obtain score information for a single screen in json format
+ [**get_screen_pandas.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_pandas.py) - Obtain score information for a single screen, and load it into a pandas dataframe
+ [**get_screens.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screens.py) - Obtain screens with various configurable search criteria 
+ [**get_screens_and_scores.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screens_and_scores.py) - Obtain screens with various configurable search criteria and then fetch the score values associated with those screens with additional search criteria
+ [**get_gene.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_gene.py) - Obtain a set of scores for a single gene with various configurable search criteria
+ [**get_genes.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_genes.py) - Obtain a set of gene scores with various configurable search criteria
+ [**get_genes_and_screens.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_genes_and_screens.py) - Obtain a set of scores for a specific gene, with configured criteria and then fetch the annotation about the screens it returned