#!/usr/bin/env python

from glob import glob
from configobj import ConfigObj
import urllib2
from urllib import urlencode
from re import compile

def packages():
    'Check config files in ./pkgs and parse the data'
    pkg_dir = './pkgs'
    packages = []
    for _file in glob("%s/*.conf" % pkg_dir):
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
        latest[p['name']] = {'package': versions[0][0], 'version': versions[0][1]}
    return latest
   
def compare_to_ius(name, p):
    'Takes the results of each object of all_latest() and compares version to IUS'
    request = urllib2.urlopen('http://dl.iuscommunity.org/pub/ius/stable/Redhat/5/SRPMS/')
    content = request.read()
    match = compile(name + '-([0-9.]*)-.*.src.rpm').findall(content)
    ius_ver = sorted(match, reverse=True)[0]
    if ius_ver <= p['version']:
        return p['version']

# Lets compare IUS version with latest upstream
packages = packages()
latest_packages = all_latest(packages)
for package in latest_packages:
    compare = compare_to_ius(package, latest_packages[package])
    if compare:
        print package, 'is out of date, upstream has', compare
