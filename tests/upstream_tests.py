from nose.tools import with_setup
import ossvt.upstream

def setup_func():
    """Setup operations before every test."""
    pass

def teardown_func():
    """Teardown operations after every test."""
    pass

@with_setup(setup_func, teardown_func)
def test_packages():
    ossvt.upstream.packages()

@with_setup(setup_func, teardown_func)
def test_package():
    ossvt.upstream.package('php52')

@with_setup(setup_func, teardown_func)
def test_latest():
    p = ossvt.upstream.package('php52')
    ossvt.upstream.latest(p[0])

@with_setup(setup_func, teardown_func)
def test_latest_url_post():
    p = ossvt.upstream.package('mysql55')
    ossvt.upstream.latest(p[0])
