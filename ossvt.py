#!/usr/bin/env python

from glob import glob
from configobj import ConfigObj
import urllib2
from urllib import urlencode
from re import compile
import sys

pkg_dir = './pkgs'
packages = []
for _file in glob("%s/*.conf" % pkg_dir):
    c = ConfigObj(_file)
    if not c['enabled'] in [True, 'True', 'true', 1, '1']:
        continue

    packages.append(c)

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
    print versions
