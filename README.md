# BioGRID ORCS Web Service Examples
Sample code for accessing the BioGRID ORCS Rest Service and working with the resulting datasets.

## Development Status
+ **Status**: Stable
+ **Version**: 2.0

## Requirements
+ Python 3.12+
+ [uv](https://docs.astral.sh/uv/) for managing Python and dependencies
+ From inside this directory, run `uv sync`. This installs the correct Python version (if needed) and all dependencies into a local `.venv`.

## Configuration
+ All configuration options are located in the config/config.sample.yml file in YAML format. Simply rename the file to config.yml and update the options contained within to reflect your own environment.
+ All access to the BioGRID ORCS Webservice requires an individual access key. It's free to signup to use it. You will need to register at **https://orcsws.thebiogrid.org/** to obtain one, and enter it in your config file for it to be accessible from all example code in this repository.
+ Alternatively, set the `ORCS_ACCESS_KEY` and `ORCS_BASE_URL` environment variables. These override `config.yml`, and if both are set the config file is not needed. Example: `ORCS_ACCESS_KEY=yourkey ORCS_BASE_URL=https://orcsws.thebiogrid.org uv run get_organisms.py`
+ For a listing of all configurable search parameters when making requests, visit our wiki: **https://wiki.thebiogrid.org/doku.php/orcs:webservice**

## How to Run
+ After completing the configuration steps above, simply run: **uv run \<script name\>** at the command prompt. Example: **uv run get_screen_tab.py**
+ All examples log their results with [Loguru](https://github.com/Delgan/loguru).

## Development
+ Code is linted and formatted with [Ruff](https://docs.astral.sh/ruff/), configured in `pyproject.toml`:
    + `uv run ruff check .`
    + `uv run ruff format .`

## Examples
+ [**uv run get_organisms.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_organisms.py) - Obtain currently supported organism ids
+ [**uv run get_vocab_terms.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_vocab_terms.py) - Obtain controlled vocabulary terms to help you create requests for other endpoints of the API
+ [**uv run get_screen_tab.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_tab.py) - Obtain score information for a single screen in tab format
+ [**uv run get_screen_json.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_json.py) - Obtain score information for a single screen in json format
+ [**uv run get_screen_pandas.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_pandas.py) - Obtain score information for a single screen, and load it into a pandas dataframe
+ [**uv run get_screen_polars.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screen_polars.py) - Obtain score information for a single screen, and load it into a polars dataframe (the same example as above, using polars)
+ [**uv run get_screens.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screens.py) - Obtain screens with various configurable search criteria 
+ [**uv run get_screens_and_scores.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_screens_and_scores.py) - Obtain screens with various configurable search criteria and then fetch the score values associated with those screens with additional search criteria
+ [**uv run get_gene.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_gene.py) - Obtain a set of scores for a single gene with various configurable search criteria
+ [**uv run get_genes.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_genes.py) - Obtain a set of gene scores with various configurable search criteria
+ [**uv run get_genes_and_screens.py**](https://github.com/BioGRID/ORCS-REST-EXAMPLES/blob/master/get_genes_and_screens.py) - Obtain a set of scores for a specific gene, with configured criteria and then fetch the annotation about the screens it returned

## Third Party Tools (Real World Examples)
The following are third party, open source tools that make use of the BioGRID ORCS API in interesting and useful ways.
+ [**ScreenHCA**](https://github.com/wujood/ScreenHCA) - A python script to cluster CRISPR screens from the BioGRID ORCS database using hierarchical clustering. 
