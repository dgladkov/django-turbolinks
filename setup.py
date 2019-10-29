#!/usr/bin/env python
from __future__ import unicode_literals

from setuptools import Command, setup, find_packages

from django_turbolinks import __version__ as version


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
    name='django-turbolinks-dj2',
    version=version,
    url='https://github.com/dbarbeau/django-turbolinks-dj2',
    license='MIT',
    author='Dmitry Gladkov',
    author_email='barbeau.daniel@outlook.com',
    description='Drop-in turbolinks implementation for Django',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=2.0',
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
