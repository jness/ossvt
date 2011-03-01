#!/usr/bin/env python

from lib.upstream import *
from lib.ius import *
from lib.launchpad import *
import argparse

class colors:
    pink = '\033[95m'
    red = '\033[91m'
    green = '\033[92m'
    gold = '\033[93m'
    blue = '\033[94m'
    end = '\033[0m'


# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Software Version to Compare', required=False)
args = parser.parse_args()

# Lets compare IUS version with latest upstream
if args.name:
    pkg = package(args.name)
else:
    pkg = packages()

# Print out our Packages and Info
print '%-30s %-15s %-15s %s' % ('name', 'ius ver', 'upstream ver', 'status')
print '='*75

for p in pkg:
    upstream_ver = latest(p)
    ius_ver = ius_version(p['name'])

    # Do the actual version comparisons
    compare = compare_to_ius(ius_ver, upstream_ver)
    if compare:
        print '%-30s %-15s %-15s %s' % (p['name'], ius_ver, upstream_ver, colors.red + 'outdated' + colors.end)
    else:
        print '%-30s %-15s %-15s %s' % (p['name'], ius_ver, upstream_ver, colors.green + 'updated' + colors.end)
