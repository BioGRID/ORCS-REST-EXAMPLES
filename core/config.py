"""
Load the config file and create any custom variables
that are available for ease of use purposes.

The ORCS_ACCESS_KEY and ORCS_BASE_URL environment variables, when set,
override the values in config/config.yml. If both are set, the config
file is optional.
"""

import os
from pathlib import Path

import yaml
from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "config" / "config.yml"

data = {"orcs": {}}
if CONFIG_FILE.exists():
    data = yaml.safe_load(CONFIG_FILE.read_text()) or data

# ACCESS KEY and BASE URL (environment variables win over the config file)
ACCESS_KEY = os.environ.get("ORCS_ACCESS_KEY") or data["orcs"].get("access_key")
BASE_URL = (os.environ.get("ORCS_BASE_URL") or data["orcs"].get("base_url") or "").rstrip("/")

if not ACCESS_KEY or not BASE_URL:
    logger.error(
        "Missing configuration: create config/config.yml from config/config.sample.yml, "
        "or set the ORCS_ACCESS_KEY and ORCS_BASE_URL environment variables."
    )
    raise SystemExit(1)
