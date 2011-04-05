#!/usr/bin/env python

from upstream import package, packages, latest
from ius import ius_stable, ius_testing
from launchpad import bug_titles, compare_titles, create_bug
from ver_compare import vcompare
import argparse
import sys

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    end = '\033[0m'

def main():
    # Build my Parser with help for user input
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='Software Version to Compare', required=False)
    args = parser.parse_args()
    
    # Configuration
    with_launchpad = False
    layout = '%-30s %-15s %-15s %s'
    layout_titles = ('name', 'ius ver', 'upstream ver', 'status')

    # Lets compare IUS version with latest upstream
    if args.name:
        pkg = package(args.name)
        with_launchpad = False
    else:
        pkg = packages()

    if pkg:
        # Print out our Packages and Info
        print layout % layout_titles
        print '='*75

        for p in pkg:
            ius_ver = ius_stable(p['name'])
            upstream_ver = latest(p)
    
            # Be sure we successfully pulled the versions
            if upstream_ver:

                # Do the actual version comparisons
                compare = vcompare(ius_ver, upstream_ver)
                if compare:
                    status = 'outdated'
                    color = colors.red

                    # Since its out of date we should check testing
                    ius_test = ius_testing(p['name'])
                    if ius_test:
                        compare_testing = vcompare(ius_test, upstream_ver)
                        if compare_testing:
                            ius_ver = ius_test
                            status = 'testing outdated'
                            color = colors.red
                        else:
                            ius_ver = ius_test
                            status = 'testing'
                            color = colors.blue


                    # If we got a IndexError testing did not have the package
                    #except IndexError:
                    #    pass
                
                else:
                    status = 'up2date'
                    color = colors.green
                
                print layout % (p['name'], ius_ver, upstream_ver, color + status + colors.end)

                # Check Launchpad if status is outdated
                if with_launchpad and status == 'outdated' or status == 'testing outdated':
                    try:
                        if titles:
                            pass
                    except:
                        # If we haven't checked LP do it now
                        titles = bug_titles()

                    if compare_titles(titles, p['name'], compare):
                        # Already in Launchpad
                        pass
                    else:
                        create_bug(p['name'], compare, p['url'])

            # If we failed to pull upstream version
            else:
                print layout % (p['name'], ius_ver, '??????', colors.red + 'unknown' + colors.end)


    else:
        print 'Not a valid package name'

if __name__ == '__main__':
    main()
