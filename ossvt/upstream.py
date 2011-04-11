from glob import glob
from configobj import ConfigObj
import urllib2
from urllib import urlencode
from re import compile
from natsort import *
import os, sys

def packages():
    '''Return a list of all packages found in pkg_dir,
the configuration will contain needed regular expressions and 
URLs to grab latest software version number.'''
    path = os.path.split(os.path.abspath(__file__))[0]
    pkg_dir = path + '/pkgs'
    packages = []
    for _file in glob("%s/*.conf" % pkg_dir):
        c = ConfigObj(_file)
        if not c['enabled'] in [True, 'True', 'true', 1, '1']:
            continue
        packages.append(c)
    return packages

def package(pkg):
    '''Return a list of one package found in pkg_dir with given pkg name,
the configuration will contain needed regular expression and
URL to grab latest software version number.'''
    path = os.path.split(os.path.abspath(__file__))[0]
    pkg_dir = path + '/pkgs'
    package = []
    for _file in glob("%s/%s.conf" % (pkg_dir, pkg)):
        c = ConfigObj(_file)
        if not c['enabled'] in [True, 'True', 'true', 1, '1']:
            continue
        package.append(c)
    return package

def latest(p):
    '''Using our list from package() or packages() we extract data to make
the needed URL request, we then take the regex to pull the latest 
software version.'''
    request = urllib2.Request(p['url'])
    try:
        post = {p['post_value']: p['post_data']}
    except KeyError:
        pass
    else:
        request.add_data(urlencode(post))

    try:
        content = urllib2.urlopen(request).read()
    except urllib2.URLError:
        return False

    versions = compile(p['regex']).findall(content)
    # simple sorted does not work with versions containing
    # more than one decimal
    #version = sorted(versions, reverse=True)[0]
    versions = natsorted(versions)
    versions.reverse()
    try:
        version = versions[0]
    except IndexError:
        return False
    else:
        return version
