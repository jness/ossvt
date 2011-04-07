from urllib import urlencode
import urllib2
from re import compile

def ius_stable(name):
    '''Using regex we pull the latest version number from the IUS RHEL5 repo '''
    request = urllib2.urlopen('http://dl.iuscommunity.org/pub/ius/stable/Redhat/5/SRPMS/')
    content = request.read()
    match = compile(name + '-([0-9.]*)-.*.src.rpm').findall(content)
    try:
        ius_ver = sorted(match, reverse=True)[0]
    except IndexError:
        return None
    else:
        return ius_ver

def ius_testing(name):
    '''Using regex we pull the latest version number from the IUS RHEL5 repo '''
    request = urllib2.urlopen('http://dl.iuscommunity.org/pub/ius/testing/Redhat/5/SRPMS/')
    content = request.read()
    match = compile(name + '-([0-9.]*)-.*.src.rpm').findall(content)
    try:
        ius_ver = sorted(match, reverse=True)[0]
    except IndexError:
        return False
    else:
        return ius_ver
