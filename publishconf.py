#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
import pelican
from pelican.plugins import sitemap, seo

installed_plugins_dir = pelican.plugins.__path__[0]   # ones that are pip installed
local_plugins_dir = 'plugins'  # ones that are in the repo

PLUGIN_PATHS = [local_plugins_dir, installed_plugins_dir]
PLUGINS = ['seo', 'sitemap']

SEO_REPORT = False
SEO_ENHANCER = True
SEO_ENHANCER_OPEN_GRAPH = True
SEO_ENHANCER_TWITTER_CARDS = True
LOGO = "https://nimbleautonomy.com/android-chrome-512x512.png"

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://nimbleautonomy.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = 'G-23PKHLZP5B'

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
