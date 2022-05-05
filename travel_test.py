from travel import Space
from nose.tools import *

def test_space():
    mars = Space("Mars", "This is a red planet, with very less water supply")
    assert_equal(mars.name, "Mars")