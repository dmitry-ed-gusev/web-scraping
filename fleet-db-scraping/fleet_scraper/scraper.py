#!/usr/bin/env python3
# coding=utf-8

"""
    Main Fleet Scraper Module for all particular scrapers

    Created:  Gusev Dmitrii, 10.01.2021
    Modified: Dmitrii Gusev, 29.04.2021
"""

# todo: https://realpython.com/python-interface/

import logging
from pyutilities.pylog import setup_logging

from engine import scraper_clarksonsnet
from engine import scraper_marinetrafficcom
from engine import scraper_rsclassorg
from engine import scraper_vesselfindercom

# some useful constants
LOGGING_CONFIG = "logging.yml"
SCRAPERS_CACHE_PATH = ""
MULTI_THREADED_WORKERS_COUNT = 20

# setup logging for the whole script
setup_logging(default_path='logging.yml')
log = logging.getLogger('fleet_scraper')


def scrap_all_data():
    log.debug("scrap_all_data(): processing various data sources.")
    scraper_clarksonsnet.scrap()      # <- scrap clarksons site
    scraper_marinetrafficcom.scrap()  # <- scrap marinetraffic site
    #scraper_rsclassorg.scrap()        # <- scrap rs-class register book (rs-class site)
    scraper_vesselfindercom.scrap()   # <- scrap vesselfinder site


# main part of the script
if __name__ == '__main__':
    log.info("Starting Fleet Scraper...")
    scrap_all_data()