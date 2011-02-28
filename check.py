#!/usr/bin/env python

from glob import glob
from configobj import ConfigObj
import urllib2
from urllib import urlencode
from re import compile
import os, sys
from launchpadlib.launchpad import Launchpad

def packages(package):
    'Check config files in ./pkgs and parse the data'
    pkg_dir = './pkgs'
    packages = []
    for _file in glob("%s/%s.conf" % (pkg_dir, package)):
        c = ConfigObj(_file)
        if not c['enabled'] in [True, 'True', 'true', 1, '1']:
            continue
        packages.append(c)
    return packages

def all_latest(packages):
    'Using the data from packages() check each source'
    latest = {}
    for p in packages:
        request = urllib2.Request(p['url'])
        try:
            post = {p['post_value']: p['post_data']}
        except KeyError:
            pass
        else:
            request.add_data(urlencode(post))

        content = urllib2.urlopen(request).read()
        versions = compile(p['regex']).findall(content)
        versions = sorted(versions, reverse=True)
        latest[p['name']] = {'version': versions[0]}
    return latest

def ius_version(name):
    'Takes the results of each object of all_latest() and gets IUS version'
    request = urllib2.urlopen('http://dl.iuscommunity.org/pub/ius/stable/Redhat/5/SRPMS/')
    content = request.read()
    match = compile(name + '-([0-9.]*)-.*.src.rpm').findall(content)
    ius_ver = sorted(match, reverse=True)[0]
    return ius_ver

def compare_to_ius(ius_ver, p):
    if ius_ver < p['version']:
        return p['version']

# Lets compare IUS version with latest upstream
packages = packages(sys.argv[1])
latest_packages = all_latest(packages)

for package in latest_packages:

    # Do the actual version comparisons
    ius_ver = ius_version(package)
    compare = compare_to_ius(ius_ver, latest_packages[package])
    if compare:
        print package, 'is out of date, we have', ius_ver, 'upstream has', compare
    else:
        print package, 'is up to date, we have', ius_ver
