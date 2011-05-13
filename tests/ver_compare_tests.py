from nose.tools import with_setup
import ossvt.ver_compare

def setup_func():
    """Setup operations before every test."""
    pass

def teardown_func():
    """Teardown operations after every test."""
    pass

@with_setup(setup_func, teardown_func)
def test_vcompare_same():
    ossvt.ver_compare.vcompare('5.0', '5.0')

@with_setup(setup_func, teardown_func)
def test_vcompare_lower():
    ossvt.ver_compare.vcompare('4.0', '5.0')

@with_setup(setup_func, teardown_func)
def test_vcompare_higher():
    ossvt.ver_compare.vcompare('6.0', '5.0')
