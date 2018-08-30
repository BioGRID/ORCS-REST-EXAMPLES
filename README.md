# BioGRID ORCS Rest Service Example Code
Sample code for accessing the BioGRID ORCS Rest Service and working with the resulting datasets.

## Development Status
+ **Status**: In Progress

## Requirements
+ Python 3.6.5+
+ Required Python libraries are listed in requirements.txt. To install them all simply run the following from within your development environment: 
  + **pip3 install -r requirements.txt**
+ We also recommend installing virtualenv and virtualenvwrapper for a containerized python environment ([**Setup Instructions**](https://askubuntu.com/questions/244641/how-to-set-up-and-use-a-virtual-python-environment-in-ubuntu/244642#244642))

## Configuration
+ All configuration options are located in the config/config.sample.yml file in YAML format. Simply rename the file to config.yml and update the options contained within to reflect your own environment.
+ All access to the BioGRID ORCS Webservice requires an individual access key. It's free to signup to use it. You will need to register at **https://orcsws.thebiogrid.org/** to obtain one, and enter it in your config file for it to be accessible from all example code in this repository.
+ For a listing of all configurable search parameters when making requests, visit our wiki: **https://wiki.thebiogrid.org/doku.php/orcs:webservice**

## Examples
+ get_screen_tab.py - Obtain score information for a single screen in tab format
+ get_screen_json.py - Obtain score information for a single screen in json format
+ get_screens.py - Obtain screens with various configurable search criteria 