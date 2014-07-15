#!/usr/bin/env python
from __future__ import print_function
import os
from tox._config import parseconfig


TRAVIS_CONFIG_FILENAME = '.travis.yml'


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    travis_config_path = os.path.join(base_dir, TRAVIS_CONFIG_FILENAME)
    with open(travis_config_path, 'w') as f:
        print("language: python", file=f)
        print("env:", file=f)
        for env in parseconfig(pkg='tox').envlist:
            print("  - TOX_ENV={}".format(env), file=f)
        print("install:", file=f)
        print("  - pip install tox", file=f)
        print("script:", file=f)
        print("  - tox", file=f)

if __name__ == '__main__':
    main()
