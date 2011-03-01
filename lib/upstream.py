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

def package(pkg):
    'Check config files in ./pkgs and parse the data'
    pkg_dir = './pkgs'
    package = []
    for _file in glob("%s/%s.conf" % (pkg_dir, pkg)):
        c = ConfigObj(_file)
        if not c['enabled'] in [True, 'True', 'true', 1, '1']:
            continue
        package.append(c)
    return package

def latest(p):
    'Using the data from package() or packages() check source'
    request = urllib2.Request(p['url'])
    try:
        post = {p['post_value']: p['post_data']}
    except KeyError:
        pass
    else:
        request.add_data(urlencode(post))

    content = urllib2.urlopen(request).read()
    versions = compile(p['regex']).findall(content)
    version = sorted(versions, reverse=True)[0]
    return version
