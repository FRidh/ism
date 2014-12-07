"""
Tests for :mod:`ism._tools`.
"""
from ism._tools import Arrow3D

class TestArrow:
    """
    Test for :class:`ism._tools.Arrow`.
    """
    
    def test_arrow(self):
        """
        """
        a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
    
    
