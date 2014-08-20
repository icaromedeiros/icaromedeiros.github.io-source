#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.icaromedeiros.com.br'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""

###
# Services
###

# Github options
GITHUB_USER = "icaromedeiros"
GITHUB_SHOW_USER_LINK = True

# Twitter feed configs
TWITTER_USERNAME = "icaromedeiros"
TWITTER_WIDGET_ID = 501159537634590722

# AddThis
ADDTHIS_PROFILE = "ra-53f14e6163baee9f"
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

# Analytics
GOOGLE_ANALYTICS = "UA-53907792-1"
