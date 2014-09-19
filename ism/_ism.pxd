cimport numpy as np
import numpy as np
from geometry.point cimport Point
from geometry.polygon cimport Polygon
from geometry.plane cimport Plane
from geometry.vector cimport Vector


cdef class Wall
cdef class Mirror

cdef class Wall(Polygon): 
    cdef public np.ndarray impedance
    """
    Impedance
    """
    
cdef class Mirror(object):
    cdef public Point position
    cdef public Mirror mother
    cdef public Wall wall
    cdef public int wall_index
    cdef public np.ndarray distance
    cdef public np.ndarray strength
    cdef public np.ndarray effective
    cdef public int order
    
    
    
