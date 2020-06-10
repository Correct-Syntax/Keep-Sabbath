Keep-Sabbath
============

Keep Sabbath is a django app to automatically redirect website visitors when it is the Sabbath day, with support for overriding on other Biblical Holy days.

!["Keep Sabbath"](keep-sabbath-logo.png?raw=true "Keep Sabbath")


# Introduction

Keep-Sabbath is for webmasters with e-commerce shops, blogs, etc. who would like to keep the Biblical 7th-day Sabbath and other Holy days of the Bible Holy. 

The django app allows you to easily setup a system for a Django-powered website that will automatically redirect visitors to a single page (explaining about the Sabbath, redirect, etc.) if it is the Sabbath day or another Holy day.

The app uses internal, offline calculations (via the SolarTime module) and the current date/time of the server to figure out if it is the Sabbath day (thus, if the user should be redirected), so you do not have to do it manually. It is optimized for performance and speed.

There is also an option to manually override it as well, which is useful for other Biblical Holy days.


# Features

  * Simple setup
  * 2 ways to use it
  * Automatically redirects when it is the 7th day Sabbath
  * Support for manual overriding
  * Supports Django 2.2, 3.0 +


# Basis

The timing is based on the understanding that the 7th-day Sabbath day starts on 6th day ("Friday") evening and ends on 7th day ("Saturday") evening, according to the Bible.

*"If thou turn away thy foot from the sabbath, from doing thy pleasure on My holy day; and call the sabbath a delight, the holy of Yahweh, honourable; and shalt honour him, not doing thine own ways, nor finding thine own pleasure, nor speaking thine own words:
Then shalt thou delight thyself in Yahweh; and I will cause thee to ride upon the high places of the earth, and feed thee with the heritage of Jacob thy father: for the mouth of Yahweh hath spoken it." -Isaiah 58:13-14*

There are many more verses regarding the importance of keeping the 7th-day Sabbath in the Bible.
django>=2.2 

``pip install django``

# Requirements

  **Python 3.5 or higher**

  * `django`_ 2.2, 3.0+
  * `pytz`

  * *(optional) ``solartime`` module*

.. _django: http://djangoproject.com


# Documentation

The latest documentation can be found at the <a href="https://correctsyntax.com/projects/keep-sabbath/">Keep-Sabbath Homepage</a>


# Development

Help improving this package to meet the project goals is always welcome. :)


# License

Keep-Sabbath is licensed under the BSD 3-Clause License. See the LICENSE for full copyright and license information.