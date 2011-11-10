#!/usr/bin/env python

from distutils.core import setup
import os

version = '0.01'

data = dict(
    name = 'zmWatcher',
    version = version,
    description = 'zmWatcher - Bridge between ZoneMinder and Zabbix.',
    author = 'David Whyte',
    author_email = 'david.whyte [at] gmail.com',

    scripts = ['zmWatcher'],
    data_files = [('/etc/init', ['zmWatcher.conf'])],
    )


setup(**data)
