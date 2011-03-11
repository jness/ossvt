from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ossvt',
      version=version,
      description="Open Source Software Version Tracker",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jeffrey Ness',
      author_email='jeffrey.ness@rackspace.com',
      url='',
      license='GPLv2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      package_data = {
          'ossvt': ['pkgs/*.conf'],
      },
      zip_safe=False,
      install_requires=[
          'configobj',
          'launchpadlib',
      ],
      entry_points= {
        'console_scripts': ['ossvt = ossvt.main:main']
        },
      )
