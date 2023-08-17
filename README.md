# Keep Sabbath

Keep Sabbath is a Django app to automatically redirect website visitors when it is the Sabbath day, with support for overriding on other Biblical Holy days.


## Introduction

Keep Sabbath is for webmasters with e-commerce shops, blogs, etc. who would like to keep the Biblical 7th-day Sabbath and other Holy days of the Bible Holy.

The django app allows you to easily setup a system for a Django-powered website that will automatically redirect visitors to a single page (explaining about the Sabbath, redirect, etc.) if it is the Sabbath day or another Holy day.

The app uses internal, offline calculations (via the SolarTime module) and the current date/time of the server to figure out if it is the Sabbath day (thus, if the user should be redirected), so you do not have to do it manually. It is optimized for performance and speed.

There is also an option to manually override it as well, which is useful for other Biblical Holy days.

The timing is based on the understanding that the 7th-day Sabbath day starts on 6th day ("Friday") evening and ends on 7th day ("Saturday") evening, according to the Bible.


## Features

- Simple setup
- 2 ways to use it
- Automatically redirects when it is the 7th day Sabbath
- Support for manual overriding
- Supports Django 3.2+


## Installation

- ``pip install keep_sabbath``
- ``pip install pytz``


## Documentation

The documentation can be found in the demo: ``example/examplewebsite``.


## Contributing

**All contributions are welcome!** Feel free to open a PR or ask questions. :)


## Releasing on PyPI

Navigate to the root directory

Run ``py -m build``

Then run ``twine upload dist/*`` and follow the prompts.


## License

Keep-Sabbath is licensed under the BSD 3-Clause License. Feel free to use as needed in your own projects. See the LICENSE for full copyright and license information.