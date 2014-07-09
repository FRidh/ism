"""
Tools.
"""

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    """
    Arrow3D.
    """
    def __init__(self, xs, ys, zs, *args, **kwargs):

        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

    @classmethod
    def from_points(cls, start, stop, *args, **kwargs):
        """
        Create arrow given a start and stop point.
        
        :param cls: Class
        :param start: Start
        :param stop: Stop
        
        """
        try:
            return cls([start.x, stop.x], [start.y, stop.y], [start.z, stop.z], *args, **kwargs)
        except AttributeError:
            return cls([start[0], stop[0]], [start[1], stop[1]], [start[2], stop[2]], *args, **kwargs)

#a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k")
