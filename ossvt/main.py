#!/usr/bin/env python

from upstream import package, packages, latest
from ius import ius_stable, ius_testing
from launchpad import bug_titles, compare_titles, create_bug
from ver_compare import vcompare
import smtplib
import argparse
import sys

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    end = '\033[0m'

class htmlcolors:
    red = '<font color=red>'
    green = '<font color=green>'
    blue = '<font color=blue>'
    end = '</font>'

# Build my Parser with help for user input
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='Software Version to Compare', required=False)
parser.add_argument('--email', action='store_true',
        dest='email', default=None,
        help='send email with results')
args = parser.parse_args()

def main():
    # Configuration
    with_launchpad = False
    global layout
    layout = '%-30s %-15s %-15s %s'
    global layout_titles
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

        global output
        output = []
        for p in sorted(pkg, key=lambda a: a['name']):
            ius_ver = ius_stable(p['name'])
            upstream_ver = latest(p)
    
            # Be sure we successfully pulled the versions
            if upstream_ver:

                # Do the actual version comparisons
                compare = vcompare(ius_ver, upstream_ver)
                if compare:
                    status = 'outdated'
                    color = colors.red
                    htmlcolor = htmlcolors.red

                    # Since its out of date we should check testing
                    ius_test = ius_testing(p['name'])
                    if ius_test:
                        compare_testing = vcompare(ius_test, upstream_ver)
                        if compare_testing:
                            ius_ver = ius_test
                            status = 'testing outdated'
                            color = colors.red
                            htmlcolor = htmlcolors.red
                        else:
                            ius_ver = ius_test
                            status = 'testing'
                            color = colors.blue
                            htmlcolor = htmlcolors.blue

                else:
                    status = 'up2date'
                    color = colors.green
                    htmlcolor = htmlcolors.green
                
                print layout % (p['name'], ius_ver, upstream_ver, color + status + colors.end)
                output.append((p['name'], ius_ver, upstream_ver, htmlcolor + status + htmlcolors.end))

                # Check Launchpad if status is outdated
                if with_launchpad:
                    if status == 'outdated' or status == 'testing outdated':
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
                output.append((p['name'], ius_ver, '??????', htmlcolors.red + 'unknown' + htmlcolors.end))


    else:
        print 'Not a valid package name'

if __name__ == '__main__':
    main()
    
    # Send Email
    if args.email:
        print '\nsending email...'
        fromaddr = ''                   # <----- Fill me in
        toaddr = ''                     # <----- Fill me in
        subject = ''                    # <----- Fill me in

        header = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n"
            % (fromaddr, toaddr, subject))
        header = header + 'MIME-Version: 1.0\r\n'
        header = header + 'Content-Type: text/html\r\n\r\n'


        body = '<pre>'
        body = body + layout % layout_titles
        body = body + '\n'
        body = body + '='*75
        body = body + '\n'

        for p in output:
            body = body + layout % (p[0], p[1], p[2], p[3])
            body = body + '\n'

        body = body + '</pre>'
        msg = header + body
        
        try:
            server = smtplib.SMTP('localhost')
            server.set_debuglevel(0)

        except:
            print "Unable to connect to SMTP server"

        else:
            server.sendmail(fromaddr, toaddr, msg)
            server.quit()
