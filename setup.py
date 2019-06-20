#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Baidu AIP SDK
"""
import platform
from setuptools import setup

setup(
    name = 'baidu-aip',
    version = '2.2.17.0',
    packages = [
        'aip',
    ],
    install_requires=[
        'requests',
    ],
    scripts = [
        'bin/aip_client',
    ] if 'Windows' not in platform.system() else [],
    license = 'Apache License',
    author = 'Baidu',
    author_email = 'aip@baidu.com',
    url = 'https://github.com/Baidu-AIP',
    description = 'Baidu AIP SDK',
    keywords = ['baidu', 'aip', 'ocr', 'antiporn', 'nlp', 'face', 'kg', 'speech'],
)
