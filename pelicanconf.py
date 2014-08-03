#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ícaro Medeiros'
SITENAME = u'Ícaro Medeiros'

# TODO how to change this when deploying?
SITEURL = ''

TIMEZONE = 'Europe/Paris'

THEME = '../pelican-bootstrap3'

# Where to look for plugins
PLUGIN_PATH = '../pelican-plugins'

# Which plugins to enable
PLUGINS = ['better_figures_and_images']

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme options

# Display tags inline (enable tag cloud)
DISPLAY_TAGS_INLINE = True

# Plugins options

RESPONSIVE_IMAGES = True
