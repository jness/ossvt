from launchpadlib.launchpad import Launchpad
import os, sys

def bug_titles():
    'Get titles for all bugs in LP'
    titles = []
    launchpad = Launchpad.login_anonymously(os.path.basename(sys.argv[0]), 'production')
    ius = launchpad.projects.search(text='ius')[0]
    tasks = ius.searchTasks()
    for task in tasks:
        titles.append(task.bug.title)
    return titles

def compare_titles(titles, name, version):
    'Compare our title with LP title'
    for title in titles:
        mytitle = 'UPDATE REQUEST: ' +  name + ' ' +  str(version) + ' is available upstream'
        if title == mytitle:
            return True

def create_bug(name, version, url):
    launchpad = Launchpad.login_with(os.path.basename(sys.argv[0]), 'production')
    ius = launchpad.projects.search(text='ius')[0]
    mytitle = 'UPDATE REQUEST: ' +  name + ' ' +  str(version) + ' is available upstream'
    launchpad.bugs.createBug(description='New Source from Upstream:', url, title=mytitle, target=ius)
