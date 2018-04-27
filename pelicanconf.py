#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'kkiyama117'
SITENAME = 'ぼっちでプログラミング。'
SITESUBTITLE = 'ひとりでできるもん！'
SITEURL = 'http://localhost:8000'

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

GITHUB_USER = "kkiyama117"
GITHUB_SHOW_USER_LINK = True

TWITTER_USER = "Muskuarede "
TWITTER_TWEET_BUTTON = True
TWITTER_FOLLOW_BUTTON = True

FACEBOOK_LIKE = True
SEARCH_BOX = True

REVERSE_CATEGORY_ORDER = True
LOCALE = "ja_JP.UTF-8"
DEFAULT_PAGINATION = 5
DEFAULT_DATE = (2018, 5, 1, 14, 0, 0)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# Blogroll
LINKS = (('About', SITEURL + "/pages/about/"),
         ('Author', SITEURL + "/pages/author/"),
         ('作りかけのゴミ(外部)', 'http://hinatan.jp/'),
         ('総合DBサーバー', 'http://backend.hinatan.jp/'),
         ('こ↑こ↓', 'http://github.hinatan.jp/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/Muskuarede'),
          ('github', 'https://github.com/kkiyama117'),)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# article like blog
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
ARTICLE_PATHS = ['blog']

DEFAULT_METADATA = {
    'status': 'draft',
}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# pages like about
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGE_PATHS = ["pages"]

# plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['related_posts', 'neighbors', 'tag_cloud', "sitemap"]
SITEMAP = {
    'format': 'xml'
}

# themes
THEME = 'themes'
THEME_STATIC_DIR = 'themes/static'
STATIC_PATHS = ['images']
