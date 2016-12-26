#!/usr/bin/env python
from __future__ import unicode_literals

import ast
import re
from setuptools import Command, setup, find_packages


_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('turbolinks/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


class Test(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from test_project import main
        main()


setup(
    name='django-turbolinks',
    version=version,
    url='https://github.com/dgladkov/django-turbolinks',
    license='MIT',
    author='Dmitry Gladkov',
    author_email='dmitry.gladkov@gmail.com',
    description='Drop-in turbolinks implementation for Django',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.6',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={'test': Test},
)
