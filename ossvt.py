#!/usr/bin/env python

from glob import glob
from configobj import ConfigObj
import urllib2
from urllib import urlencode
from re import compile
import os, sys
from launchpadlib.launchpad import Launchpad

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
        versions = sorted(versions, reverse=True)
        latest[p['name']] = {'version': versions[0]}
    return latest
   
def compare_to_ius(name, p):
    'Takes the results of each object of all_latest() and compares version to IUS'
    request = urllib2.urlopen('http://dl.iuscommunity.org/pub/ius/stable/Redhat/5/SRPMS/')
    content = request.read()
    match = compile(name + '-([0-9.]*)-.*.src.rpm').findall(content)
    ius_ver = sorted(match, reverse=True)[0]
    if ius_ver < p['version']:
        return p['version']

def bug_titles():
    'Get titles for all bugs in LP'
    titles = []
    launchpad = Launchpad.login_anonymously(os.path.basename(sys.argv[0]), 'production')
    ius = launchpad.projects.search(text='ius')[0]
    tasks = ius.searchTasks()
    for task in tasks:
        titles.append(task.bug.title)
    return titles

def compare_titles(titles, name, version):
    'Compare our title with LP title'
    for title in titles:
        mytitle = 'UPDATE REQUEST: ' +  name + ' ' +  str(version) + ' is available upstream'
        if title == mytitle:
            return True

def create_bug(name, version):
    launchpad = Launchpad.login_with(os.path.basename(sys.argv[0]), 'production')
    ius = launchpad.projects.search(text='ius')[0]
    mytitle = 'UPDATE REQUEST: ' +  name + ' ' +  str(version) + ' is available upstream'
    launchpad.bugs.createBug(description='New Source from Upstream:', title=mytitle, target=ius)

# Lets compare IUS version with latest upstream
packages = packages()
latest_packages = all_latest(packages)

for package in latest_packages:

    # Do the actual version comparisons
    compare = compare_to_ius(package, latest_packages[package])
    if compare:

        # See if we checked LP Yet
        try:
            if titles:
                pass
        except:
            # If we haven't checked LP do it now
            titles = bug_titles()

        if compare_titles(titles, package, compare):
            # Our version is outdated and a LP bug does not exist
            print 'Bug Already Created'
        else:
            print 'Creating Launchpad Bug for', package
            #create_bug(package, compare)
    else:
        print package, 'is up to date'
