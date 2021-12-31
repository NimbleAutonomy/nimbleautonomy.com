#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Kevin Goldsmith'
SITENAME = 'Nimble Autonomy'
SITEURL = 'https://nimbleautonomy.com'

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

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (('home', '/'),
             ('consulting', '/consulting.html'),
             ('speaking', '/speaking.html'),
             ('writing', '/articles/'),
             ('contact', '/contact.html'))
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/nimbleautonomy'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# SEO Plugin stuff
SEO_REPORT = True
SEO_ENHANCER = False

# set new root
BLOG_ROOT_PATH = 'articles/'

ARTICLE_PATHS = ['articles']
ARTICLE_URL = BLOG_ROOT_PATH + '{slug}.html'
ARTICLE_SAVE_AS = BLOG_ROOT_PATH + '{slug}.html'

AUTHOR_SAVE_AS = ''
AUTHOR_URL = ''
AUTHORS_SAVE_AS = ''
AUTHORS_URL = ''
DAY_ARCHIVE_SAVE_AS = ''
ARCHIVES_SAVE_AS = BLOG_ROOT_PATH + 'archives.html'
ARCHIVES_URL = BLOG_ROOT_PATH + 'archives.html'
CATEGORIES_SAVE_AS = BLOG_ROOT_PATH + 'categories.html'
CATEGORIES_URL = BLOG_ROOT_PATH + 'categories.html'
TAGS_SAVE_AS = BLOG_ROOT_PATH + 'tags.html'
TAGS_URL = BLOG_ROOT_PATH + 'tags.html'
CATEGORY_SAVE_AS = BLOG_ROOT_PATH + 'category/{slug}.html'
CATEGORY_URL = BLOG_ROOT_PATH + 'category/{slug}.html'
TAG_SAVE_AS = BLOG_ROOT_PATH + 'tag/{slug}.html'
TAG_URL = BLOG_ROOT_PATH + 'tag/{slug}.html'
INDEX_SAVE_AS = BLOG_ROOT_PATH + 'index.html'

STATIC_PATHS = ['images', 'extra', 'articles/images']
EXTRA_PATH_METADATA = {}
for file in os.listdir('content/extra'):
    EXTRA_PATH_METADATA[f'extra/{file}'] = { 'path': file }

TWITTER_USERNAME = 'nimbleautonomy'

THEME = "themes/forty"

DEFAULT_PAGINATION = 10
