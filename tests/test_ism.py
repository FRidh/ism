"""
Tests for :mod:`ism`.
"""
import pytest
import numpy as np
from ism import Model, Wall
from geometry import Point
import tempfile
import pickle

@pytest.fixture
def impedance1():
    bands = 10
    return np.ones(bands) + np.ones(bands)*1j

@pytest.fixture
def wall1(impedance1):
    corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
    return Wall(corners1, Point(0.5, 0.5, 0.0), impedance1)

class TestWall:

    def test_mirror(self, wall1):
        assert wall1.mirror().points == wall1.points[::-1]

class TestConcave:
    """Tests for :class:`ism.Model`.
    """

    def test_no_surfaces(self):
        """
        A model without any surfaces should not run.
        """

        S = [Point(0.9, 0.5, 0.5)]
        R = [Point(0.1, 0.501, 0.501)]

        walls = []
        model = Model(walls, S, R)
        with pytest.raises(ValueError):
            list(model.mirrors())

    def test_single_surface(self, impedance1):
        """
        A model with a single surface. Both source and receiver are positioned above the surface, slightly out of the center along the x-axis.
        In this case we except one mirror source and thus two sources in total.
        """
        S = [Point(0.7, 0.5, 0.5)]
        R = [Point(0.3, 0.501, 0.501)]

        corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
        wall1 = Wall(corners1, Point(0.5, 0.5, 0.0), impedance1)

        model = Model([wall1], S, R, max_order=3)#

        mirrors = list(model.mirrors())

        # One reflecting surface should give one mirror source, so in total two sources.
        assert(len(mirrors)==2)

        mirrors = model.determine()

        # Both sources should be effective as well.
        for mirror in mirrors:
            assert( mirror.effective.all() == True )

    def test_single_surface_wrong_orientation(self, impedance1):
        """
        A model with a single surface, like the test above. The difference here is that the surface is oriented in the wrong direction.
        Therefore, there should not be any additional mirror sources.
        """
        S = [Point(0.7, 0.5, 0.5)]
        R = [Point(0.3, 0.501, 0.501)]

        corners1m = [ Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(1.0, 1.0, 0.0), Point(1.0, 0.0, 0.0) ]
        wall1m = Wall(corners1m, Point(0.5, 0.5, 0.0), impedance1)

        model = Model([wall1m], S, R, max_order=10)

        mirrors = list(model.mirrors())

        # Because the surface is inverted we don't expect any more sources.
        assert( len(mirrors) == 1)

        mirrors = list(model.determine())

        # We have only the direct contribution, and this is effective.
        assert( mirrors[0].effective.all() == True )


    def test_single_surface_receiver_both_sides(self, impedance1):
        """
        A model with one surface. Initially the receiver is on the correct side of the surface, but is then moved to the wrong side.
        """
        S = [Point(0.7, 0.5, 0.5)]
        R = [Point(0.3, 0.501, 0.501), Point(0.3, 0.501, 0.501)]

        corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
        wall1 = Wall(corners1, Point(0.5, 0.5, 0.0), impedance1)

        model = Model([wall1], S, R, max_order=10)

        mirrors = list(model.mirrors())

        """One reflecting surface should give an additional so two sources."""
        assert( len(mirrors) == 2)

        mirrors = model.determine()

        """And both are effective."""
        for mirror in mirrors:
            assert(mirror.effective.all() == True )


class TestConvex:
    pass

def test_pickle(impedance1):
    corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
    wall = Wall(corners1, Point(0.5, 0.5, 0.0), impedance1)

    with tempfile.TemporaryDirectory() as tmpdirname:
        with open('obj.pickle', mode='w+b') as f:
            pickle.dump(wall, f)

        with open('obj.pickle', mode='r+b') as f:
            wall2 = pickle.load(f)

        assert wall2 == wall
