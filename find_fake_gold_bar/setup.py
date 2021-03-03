import sys
from setuptools import setup, find_packages

version = sys.version_info
if version == (3, 7):
    sys.stderr.write('requires Python 3.7\n')
    sys.exit(1)

PACKAGE_NAME = "find_fake_gold_bar"
PACKAGE_VERSION = "1.0"

SUMMARY = "Web Automation Framework and find_fake_bar test"

DESCRIPTION = "The framework allows to find fake gold bar from 9 bar by weighing the bars"

dependencies = ['selenium']

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      author="EvgT",
      description=SUMMARY,
      long_description=DESCRIPTION,
      packages=find_packages(),
      install_requires=dependencies)
