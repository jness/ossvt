from nose.tools import with_setup
import ossvt.ius

def setup_func():
    """Setup operations before every test."""
    pass

def teardown_func():
    """Teardown operations after every test."""
    pass

@with_setup(setup_func, teardown_func)
def test_ius_stable_index_error():
    ossvt.ius.ius_stable('nothere')

@with_setup(setup_func, teardown_func)
def test_ius_testing_index_error():
    ossvt.ius.ius_testing('nothere')

@with_setup(setup_func, teardown_func)
def test_ius_stable():
    ossvt.ius.ius_stable('php52')

@with_setup(setup_func, teardown_func)
def test_ius_testing():
    ossvt.ius.ius_testing('mysql55')
