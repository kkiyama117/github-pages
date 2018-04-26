#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kkiyama117'
SITENAME = 'じゃなきゃお前がやるんだよ'
SITESUBTITLE = 'じゃなきゃお前がやるんだよ'
SITEURL = 'localhost'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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
# RELATIVE_URLS = True

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['related_posts', 'tag_cloud','neighbors']

# themes
THEME = 'themes/pelican-striped-html5up'
STATIC_PATHS = ['images']
