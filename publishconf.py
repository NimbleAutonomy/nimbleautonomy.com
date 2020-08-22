#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
from pelican.plugins import sitemap

PLUGINS = [ 'pelican.plugins.sitemap' ]

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://nimbleautonomy.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = 'UA-175171484-1'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.8,
        'pages': 1.0,
        'indexes': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'pages': 'weekly',
        'indexes': 'daily'
    }
}
