import numpy as np

from geometry import Point

from acoustics.ism import ism, Model, Wall

import logging

def print_mirrors(mirrors):
    
    for m in mirrors:
        print('Order: {} - Effective: {} - Position: {} - Factor {}'.format(m.order, m.effective, m.position, m.strength.max()))
    
   
def create_walls():
    
    #center = 0.0
    #l_x = 1.0
    #l_y = 1.0
    #l_z = 1.0
    
    #point1 = Point(-l_x/2.0, -l_x/2.0, -l_z/2.0)
    #point2 = Point(+l_x/2.0, -l_x/2.0, -l_z/2.0)
    #point3 = Point(+l_x/2.0, +l_y/2.0, -l_z/2.0)
    #point4 = Point(-l_x/2.0, +l_y/2.0, -l_z/2.0)
    #point5 = Point(-l_x/2.0, -l_y/2.0, +l_z/2.0)
    #point6 = Point(-l_x/2.0, +l_y/2.0, +l_z/2.0)
    #point7 = Point(+l_x/2.0, +l_y/2.0, +l_z/2.0)
    #point8 = Point(+l_x/2.0, -l_y/2.0, +l_z/2.0)
    
    #wall1 = 
    
    
    impedance = 40.0 * np.ones(10)
    
    #impedance = np.ndarray([1.0])
    
    #corners1 = [ Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(1.0, 1.0, 0.0), Point(1.0, 0.0, 0.0) ]
    corners1 = [ Point(0.0, 0.0, 0.0), Point(1.0, 0.0, 0.0), Point(1.0, 1.0, 0.0), Point(0.0, 1.0, 0.0) ]
    wall1 = Wall(corners1, impedance, Point(0.5, 0.5, 0.0))
    
    #corners2 = [ Point(0.0, 0.0, -1.0), Point(0.0, 1.0, -1.0), Point(0.0, 1.0, 0.0), Point(0.0, 0.0, 0.0) ]
    corners2 = [ Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(0.0, 1.0, 1.0), Point(0.0, 0.0, 1.0) ]
    wall2 = Wall(corners2, impedance, Point(0.0, 0.5, 0.5))
    
    #corners3 = [ Point(0.0, 0.0, 1.0), Point(1.0, 0.0, 1.0), Point(1.0, 1.0, 1.0), Point(0.0, 1.0, 1.0) ]
    corners3 = [ Point(0.0, 0.0, 0.0), Point(0.0, 0.0, 1.0), Point(1.0, 0.0, 1.0), Point(1.0, 0.0, 0.0) ]
    wall3 = Wall(corners3, impedance, Point(0.5, 0.0, 0.5))
    
    corners4 = [ Point(0.0, 0.0, 1.0), Point(0.0, 1.0, 1.0), Point(1.0, 1.0, 1.0), Point(1.0, 0.0, 1.0) ]
    wall4 = Wall(corners4, impedance, Point(0.5, 0.5, 1.0))
    
    corners5 = [ Point(1.0, 0.0, 0.0), Point(1.0, 0.0, 1.0), Point(1.0, 1.0, 1.0), Point(1.0, 1.0, 0.0) ]
    wall5 = Wall(corners5, impedance, Point(1.0, 0.5, 0.5))
    
    corners6 = [ Point(0.0, 1.0, 0.0), Point(1.0, 1.0, 0.0), Point(1.0, 1.0, 1.0), Point(0.0, 1.0, 1.0) ]
    wall6 = Wall(corners6, impedance, Point(0.5, 1.0, 0.5))
    
    corners1_mirrored = [ Point(0.0, 0.0, 0.0), Point(0.0, 1.0, 0.0), Point(1.0, 1.0, 0.0), Point(1.0, 0.0, 0.0) ]
    wall1_mirrored = Wall(corners1_mirrored, impedance, Point(0.5, 0.5, 0.0))
    
    corners4_mirrored = [ Point(0.0, 0.0, 1.0), Point(1.0, 0.0, 1.0), Point(1.0, 1.0, 1.0), Point(0.0, 1.0, 1.0) ]
    wall4_mirrored = Wall(corners4_mirrored, impedance, Point(0.5, 0.5, 1.0))
    

    #walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall1_mirrored, wall4_mirrored]
    
    #walls = [wall1, wall1_mirrored]
    walls = [wall1, wall2, wall3, wall4, wall5, wall6]
    
    
    return walls
    
    
def test():
    
    logfile = 'ism.log'
    
    with open(logfile, 'w'):
        pass
    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    
    S = Point(0.9, 0.5, 0.5)
    R = [Point(0.1, 0.501, 0.501)]
    R = [ Point(0.1, 0.501, 0.501), Point(0.4, 0.501, 0.501), Point(1.9, 0.501, 0.501) ]
    
    walls = create_walls()
    
    #mirrors = ism(walls, S, R, max_order=2, max_distance=1.0e9)
    
    
    model = Model(walls, S, R, max_order=3)
    
    model.determine_mirrors().determine_effectiveness()
    
    print R
    
    for mirror in model.sort():
        print mirror.effective, mirror.strength.max(), mirror.position
    
    
    #for mirror in mirrors:
        #print mirror.effective, mirror.strength.max()
    #print model.effectiveness
    
    #for wall in walls:
        #print wall.normal()
    
    #print "Sources: {} - Effective: {}".format(len(mirrors), sum(True for mirror in mirrors if mirror.effective))
    #R = Point(100.5, 0.5, -10.9)
    
    #for i in range(60*1):
        #update_ism(mirrors, S, R)
    #print "Sources: {} - Effective: {}".format(len(mirrors), sum(True for mirror in mirrors if mirror.effective))
    
    #mirrors.sort(key= lambda x: x.strength.max() , reverse=True)
    
    #print_mirrors(mirrors)
 

 
def main():
    
    test()
    
    
if __name__ == '__main__':
    main()