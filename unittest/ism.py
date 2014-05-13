
import unittest

import numpy as np

from acoustics.ism import Model, Wall

from geometry import Point

class ModelCase(unittest.TestCase):
    
    def test_no_surfaces(self):
        """
        A model without any surfaces should not run.
        """
        
        S = Point(0.9, 0.5, 0.5)
        R = [Point(0.1, 0.501, 0.501)]
        
        walls = []
        model = Model(walls, S, R, max_order=10)
        
        self.assertRaises(ValueError, model.determine_mirrors)
        
    def test_single_surface(self):
        """
        A model with one surface with the right normal causes a reflection.
        """
        
        S = Point(0.7, 0.5, 0.5)
        R = [Point(0.3, 0.501, 0.501)]
        
        impedance1 = np.ones(10)
        
        corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
        wall1 = Wall(corners1, impedance1, Point(0.5, 0.5, 0.0))
    
        model = Model([wall1], S, R, max_order=10)
        
        mirrors = model.determine_mirrors().mirrors
        
        """One reflecting surface should give an additional so two sources."""
        self.assertEqual(len(mirrors), 2)
        
        mirrors = model.determine_mirrors().determine_effectiveness().mirrors
        
        """And both are effective."""
        for mirror in mirrors:
            self.assertTrue(mirror.effective.all())
        
    def test_single_surface_wrong_orientation(self):
        """
        A model with one surface oriented in the wrong direction.
        """
        S = Point(0.7, 0.5, 0.5)
        R = [Point(0.3, 0.501, 0.501)]
        
        impedance1 = np.ones(10)
        
        corners1m = [ Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(1.0, 1.0, 0.0), Point(1.0, 0.0, 0.0) ]
        wall1m = Wall(corners1m, impedance1, Point(0.5, 0.5, 0.0))
        
        model = Model([wall1m], S, R, max_order=10)
        
        mirrors = model.determine_mirrors().mirrors
        
        """One reflecting surface should give an additional so two sources."""
        self.assertEqual(len(mirrors), 1)
        
        mirrors = model.determine_mirrors().determine_effectiveness().mirrors
        
        """And this mirror source is effective."""
        self.assertTrue(mirrors[0].effective.all())
    
    
    def test_single_surface_receiver_both_sides(self):
        """
        A model with one surface. Initially the receiver is on the correct side of the surface, but is then moved to the wrong side.
        """
        
        S = Point(0.7, 0.5, 0.5)
        R = [Point(0.3, 0.501, 0.501), Point(0.3, 0.501, 0.501)]
        
        impedance1 = np.ones(10)
        
        corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
        wall1 = Wall(corners1, impedance1, Point(0.5, 0.5, 0.0))
    
        model = Model([wall1], S, R, max_order=10)
        
        mirrors = model.determine_mirrors().mirrors
        
        """One reflecting surface should give an additional so two sources."""
        self.assertEqual(len(mirrors), 2)
        
        mirrors = model.determine_mirrors().determine_effectiveness().mirrors
        
        """And both are effective."""
        for mirror in mirrors:
            print mirror.effective
            #self.assertTrue(mirror.effective.all())
    
    
if __name__ == '__main__':
    unittest.main()
    
    