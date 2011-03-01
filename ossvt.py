#!/usr/bin/env python
from lib.upstream import *
from lib.ius import *
from lib.launchpad import *

# Lets compare IUS version with latest upstream
packages = packages()

for p in packages:
    upstream_ver = latest(p)
    ius_ver = ius_version(p['name'])

    # Do the actual version comparisons
    compare = compare_to_ius(ius_ver, upstream_ver)
    if compare:

        # See if we checked LP Yet
        try:
            if titles:
                pass
        except:
            # If we haven't checked LP do it now
            titles = bug_titles()

        if compare_titles(titles, p['name'], compare):
            # Our version is outdated and a LP bug does not exist
            print 'Bug Already Created'
        else:
            print ' Creating Launchpad Bug for', p['name']
            #create_bug(package, compare)
    else:
        print p['name'], 'is up to date'
