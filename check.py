#!/usr/bin/env python

from lib.upstream import *
from lib.ius import *
import sys

# Lets compare IUS version with latest upstream
pkg = package(sys.argv[1])

for p in pkg:
    upstream_ver = latest(p)
    ius_ver = ius_version(p['name'])

    # Do the actual version comparisons
    compare = compare_to_ius(ius_ver, upstream_ver)
    if compare:
        print p['name'], 'is out of date, we have', ius_ver, 'upstream has', compare
    else:
        print p['name'], 'is up to date, we have', ius_ver, 'upstream has', upstream_ver
