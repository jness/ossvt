#!/usr/bin/env python
from lib.upstream import *
from lib.ius import *

# Lets compare IUS version with latest upstream

print '''To: jeffrey.ness@rackspace.com
From: IUS Coredev <ius-coredev@lists.launchpad.net>
Subject: IUS Package Versions
Content-Type: text/html; charset="us-ascii"

<pre>
'''
print '''If a package below contains a upstream ver, the 
package is out of date and should be updated

'''

print '%-25s %-15s %-10s' % ('Name', 'IUS Ver', 'Upstrem Ver')
print "="*65

packages = packages()

for p in sorted(packages, key=lambda packages: packages['name']):
    upstream_ver = latest(p)
    ius_ver = ius_version(p['name'])

    # Do the actual version comparisons
    compare = compare_to_ius(ius_ver, upstream_ver)

    if compare:
        print '%-25s %-15s %-10s' % (p['name'], ius_ver, compare)
    else:
        print '%-25s %-15s' % (p['name'], ius_ver)

print '</pre>'
