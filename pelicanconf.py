#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'ooxxvv.tw'
SITENAME = u'ooxxvv.tw'
SITESUBTITLE = u'我的傲慢與偏見'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output/'

THEME = "themes/SoMA2"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Static paths
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Default metadata
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = ' %Y.%m.%d '
DEFAULT_CATEGORY = 'None'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
