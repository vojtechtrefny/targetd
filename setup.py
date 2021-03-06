#!/usr/bin/env python

from distutils.core import setup

setup(
    name='targetd',
    version='0.8.9',
    description='Linux remote storage API daemon',
    license='GPLv3',
    maintainer='Andy Grover',
    maintainer_email='andy@groveronline.com',
    url='http://github.com/open-iscsi/targetd',
    packages=['targetd'],
    scripts=['scripts/targetd'])
