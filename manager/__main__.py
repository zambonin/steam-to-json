#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""__main__.py

The main file for a Python module that outputs detailed information about a
Steam library to a Google Drive spreadsheet.
"""

from json import load, decoder
from sys import argv
from .data_composer import shape
from .data_conveyor import upload

try:
    PRIVATE_DATA = load(open(argv[1]))
    CELLS = shape(PRIVATE_DATA['steam_api_key'], PRIVATE_DATA['steamid'],
                  PRIVATE_DATA['steam_login'], PRIVATE_DATA['prices_file'],
                  PRIVATE_DATA['country_code'])
    upload(CELLS, PRIVATE_DATA['google_api_key'],
           PRIVATE_DATA['spreadsheet_key'])
except (IndexError, FileNotFoundError, decoder.JSONDecodeError):
    raise SystemExit("Valid configuration file needed!")
