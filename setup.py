#!/usr/bin/env python
import os
import sys
from setuptools import Command, setup
import turbolinks


class test(Command):
    description = 'Custom test runner'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from run_tests import main
        main()


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

setup(
    name='django-turbolinks',
    version=turbolinks.__version__,
    url='https://github.com/dgladkov/django-turbolinks',
    license='MIT',
    author='Dmitry Gladkov',
    author_email='dmitry.gladkov@gmail.com',
    description='Drop-in turbolinks implementation for Django',
    long_description=open(
        os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    packages=['turbolinks'],
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
    test_suite='run_tests',
    cmdclass={'test': test},
)
