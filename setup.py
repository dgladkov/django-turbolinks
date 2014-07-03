#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name='django-turbolinks',
    version='0.0.2',
    description='Drop-in turbolinks implementation for Django.',
    long_description=open('README.md').read(),
    author='Dmitry Gladkov',
    author_email='dmitry.gladkov@gmail.com',
    url='https://github.com/dgladkov/django-turbolinks',
    packages=['turbolinks'],
    license='MIT',
    classifiers=(
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
