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
PLUGIN_PATHS = ['pelican-plugins']

# Which plugins to enable
PLUGINS = ['better_figures_and_images', 'pelican_youtube', 'microdata', 'simple_footnotes']

DEFAULT_LANG = u'en'
LOCALE = 'en_US'

DEFAULT_CATEGORY = "Blog"
REVERSE_CATEGORY_ORDER = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# # Blogroll
# LINKS = (
#     ('Renan Oliveira', 'http://renanoliveira.net/'),
#     loop infinito
#     dave
#     flavio
#     ('schema.org', 'http://blog.schema.org/'),
#     ('Coding horror', 'http://blog.codinghorror.com/'),
#     ('Many Sporny', 'http://manu.sporny.org/'),
#     ('Markus Lanthaler', 'http://www.markus-lanthaler.com/'),
#     ('Ruven Verborgh', 'http://ruben.verborgh.org/'),
#     ('Tall Eye', 'http://talleye.com/'),
# )

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

SHOW_ARTICLE_CATEGORY = True
SHOW_ARTICLE_AUTHOR = False  # My name is all over it

DEFAULT_DATE_FORMAT = ('%d %B %Y')

###
# Translations
##

LANG_CONFIG = {
    "pt": {
        "lang_label": u"Português",
        "lang_text": "Also available in"
    },
    "en": {
        "lang_label": "English",
        "lang_text": u"Também disponível em"
    }
}
