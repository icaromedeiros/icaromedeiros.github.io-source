#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ícaro Medeiros'
SITENAME = u'Ícaro Medeiros'

# TODO how to change this when deploying?
SITEURL = ''

TIMEZONE = 'Europe/Paris'

THEME = 'pelican-bootstrap3'

# Where to look for plugins
PLUGIN_PATH = 'pelican-plugins'

# Which plugins to enable
PLUGINS = ['better_figures_and_images', 'github_activity']

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('You can modify those links in your config file', '#'),)
# http://blog.schema.org/
# http://manu.sporny.org/
# http://ruben.verborgh.org/

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/icaromedeiros'),
          ('linkedin', 'http://www.linkedin.com/in/icaromedeiros'),
          ('github', 'http://github.com/icaromedeiros'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

###
# Theme options
###

BOOTSTRAP_THEME = 'sandstone'

# Breadcrumbs in articles
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

STATIC_PATHS = ['images']  # , 'extra/robots.txt', 'extra/favicon.ico']

# EXTRA_PATH_METADATA = {
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'}
# }

# Display tags inline (enable tag cloud)
DISPLAY_TAGS_INLINE = True

# Coding theme
PYGMENTS_STYLE = 'monokai'

# Paging without page number
USE_PAGER = True

# Github options
GITHUB_USER = "icaromedeiros"
GITHUB_SHOW_USER_LINK = True

# Twitter feed configs
TWITTER_USERNAME = "icaromedeiros"
TWITTER_WIDGET_ID = 501159537634590722

# AddThis
ADDTHIS_PROFILE = "ra-53f14e6163baee9f"
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

# TODO opengraph

###
# Plugins options
###

RESPONSIVE_IMAGES = True
