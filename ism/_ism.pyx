cimport numpy as np
import numpy as np
from geometry.core cimport Point, Polygon, Plane


cdef class Wall(Polygon):
    """
    An object describing a wall.
    
    """

    #cdef public np.ndarray impedance
    
    def __init__(self, list corners, np.ndarray[np.float64_t, ndim=1] impedance, Point center):
        """
        Constructor.
        """
        
        super(Wall, self).__init__(corners, center)

        self.impedance = impedance
        """
        Impedance of the wall.
        """
  
    def __richcmp__(self, other, int op):
        
        if not(op==2 or op==3):
            raise TypeError()
        
        if not isinstance(other, Wall):
            return False
        
        equal = True if (self.points==other.points and self.center==other.center and np.all(self.impedance==other.impedance)) else False
        
        if (op==2 and equal==True) or (op==3 and equal==False): # a == b
            return True
        else:
            return False

cdef class Mirror(object):
    """
    Temporary object that stores information of a mirror source.
    
    This is the ``qslist`` object.
    """    
    
    #cdef public Point position
    #cdef public Mirror mother
    #cdef public Wall wall
    #cdef public int order
    
    #cdef public np.ndarray effective
    #cdef public np.ndarray distance
    #cdef public np.ndarray strength


    def __init__(self, Point position, Mirror mother, Wall wall, int order):
        """
        Constructor
        """
        
        self.position = position
        """
        Position of the source.
        """
    
        self.mother = mother
        """
        Reference to the mother source.
        """
        
        self.wall = wall
        """
        Generating wall. (So that's the wall it's mirrored at, right?)
        """
        self.order = order
        """
        Order.
        """
        
        self.effective = None
        """
        Whether the mirror is an effective source (flag=0, True) or not.
        """
        
        self.distance = None
        """
        Distance between this mirror source and the receiver.
        """
        
        self.strength = None
        """
        Source strength(factor).
        """
        

cpdef int is_shadowed(Point source, Point receiver, list walls):
    """
    Test whether the receiver is shadowed by any of the walls.
    
    We need to test whether the source can see the receiver.
    If any of the walls doesn't block line of sight, and if the receiver is in the field angle,
    then the receiver is not shadowed and thus the source is effective.
    
    So we need to test using a field angle.
    
    And we need to test whether no objects are in between.
    """
    
    
    for wall in walls:
        #logging.debug("Wall {}".format(wall.plane()))
        if (source.on_interior_side_of(wall.plane()) == +1) :#and not (receiver.on_interior_side_of(wall.plane()) == +1):
            if receiver.in_field_angle(source, wall, Plane.from_normal_and_point(wall.plane().normal(), receiver)):
                intersection = wall.plane().intersection(source, receiver)
                if ((intersection-source).norm() < (receiver-source).norm())  \
                and ((intersection-receiver).norm() < (receiver-source).norm()) :    # Wall is actually in between source and receiver.
                    return 1 
    else:
        return 0

cpdef test_effectiveness(list walls, Point source_position, Point receiver_position, Point mirror_position, Wall mirror_wall, np.ndarray mother_strength):
    """
    Test the effectiveness of a mirror at a receiver location.
    """
    
    
    f = len(walls[0].impedance)
    
    distance = mirror_position.distance_to(receiver_position)
    
    effective = not is_shadowed(mirror_position, receiver_position, walls)
    
    """Strength is 1 for the zeroth order source."""
    if not mirror_wall:
        return effective, np.ones(f), distance

    cos_angle = mirror_wall.plane().normal().cosines_with(source_position.cosines_with(receiver_position))   # Cosine of the angle between the line of sight and the wall normal.
    
    try:
        refl = (mirror_wall.impedance*cos_angle - 1.0) / (mirror_wall.impedance*cos_angle + 1.0)    # Reflection coefficient
    except ZeroDivisionError:   # If angle of incidence is 90 degrees, then cos_angle is 0.0. With hard reflection this results in a division by zero.
        refl = 1.0
    
    strength = mother_strength * refl   # Amplitude strength due to current and past reflections
    
    return effective, strength, distance  

        
        

        
        
        
