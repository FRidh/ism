cimport numpy as np
import numpy as np
from geometry.core cimport Point, Polygon
from geometry.core import Point, Polygon

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
    
    
    