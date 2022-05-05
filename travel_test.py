from travel import Space
from numpy import testing as npt

def test_space():
    mars = Space("Mars", "This is a red planet, with very less water supply")
    npt.assert_equal(mars.name, "Mars")
    npt.assert_equal(mars.path, [])

def test_travel_path():
    middle = Space("Middle", "You are in middle of space")
    up = Space("Up", "You went upwards direction")
    down = Space("down", "You went downwards direction")

    middle.add_path['up': up, 'down': down]
    npt.assert_equal(middle.travel('up'), up)
    npt.assert_equal(middle.travel('down'), down)
