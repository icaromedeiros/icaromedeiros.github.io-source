#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ícaro Medeiros'
SITENAME = u'Ícaro Medeiros'
DESCRIPTION = u"Ícaro Medeiros blog - Software Engineer"

SITEURL = ''

TIMEZONE = 'America/Sao_Paulo'

THEME = 'pelican-bootstrap3'

# Where to look for plugins
PLUGIN_PATH = 'pelican-plugins'

# Which plugins to enable
PLUGINS = ['better_figures_and_images', 'pelican_youtube', 'microdata']

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = "Blog"
REVERSE_CATEGORY_ORDER = False

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
# http://talleye.com/
# Renan


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

# Show 'about me'
SHOW_ABOUTME = True
ABOUT_ME = """
Software Engineer at <a href="http://www.globo.com">Globo.com</a><br/>
PhD candidate at <a href="http://www.inf.puc-rio.br">PUC-RIO</a><br/>
"""

# Avatar
OPEN_GRAPH_IMAGE = AVATAR = "images/avatar.png"

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

DISQUS_SITENAME = "icaromedeiros"

###
# Plugins options
###

RESPONSIVE_IMAGES = True

MICRODATA_VOCABULARY = "http://schema.org"
