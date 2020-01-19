import math
import numpy as np
import random
 
def NN_vectors(coords, pix):
    """prints the distnace to the first, second and third nearest neighbour of each (x,y)
    in coords as well as the angles between the first and second, and first and third nearest neighbours"""
    T = coords
    print("NN1","NN2","NN3","angle1","angle2")
    for t1 in T:
        vals = []
        for t2 in T:
            vals.append(np.sqrt((t1[0]-t2[0])**2+(t1[1]-t2[1])**2))
         
        vals_original = [e for e in vals]
        vals.pop(vals.index(min(vals))) # this is just zero
        NN1 = min(vals)
        angle1 = 0     
        NN1_ind = vals_original.index(NN1)
        NN1_angle = np.angle(complex(T[NN1_ind][0]-t1[0],T[NN1_ind][1]-t1[1]),1) # actual angle in degrees
        vals.pop(vals.index(NN1))
        NN1_vector = [NN1,0]
         
         
        NN2 = min(vals)
        NN2_ind = vals_original.index(NN2)
        angle2 = (np.angle(complex(T[NN2_ind][0]-t1[0],T[NN2_ind][1]-t1[1]),1)-NN1_angle)%360 # angle relative to NN1
        if angle2 >= 180:
            angle2 = 360-angle2
        vals.pop(vals.index(NN2))
        NN2_vector = [NN2*np.cos(angle2),NN2*np.sin(angle2)]
         
         
        NN3 = min(vals)
        NN3_ind = vals_original.index(NN3)
        angle3 = (np.angle(complex(T[NN3_ind][0]-t1[0],T[NN3_ind][0]-t1[1]),1)-NN1_angle)%360#-NN1_angle # angle relative to NN1
        if angle3 >= 180:
            angle3 = 360-angle3
        
        vals.pop(vals.index(NN3))
        NN3_vector = [NN3*np.cos(angle3),NN3*np.sin(angle3)]

         
        print(pix*NN1,pix*NN2,pix*NN3, angle2, angle3)
 

data = open(r"./coordinates_data.csv").readlines()
coordinates = []
for line in data[1:]:
    f = line.split(",")
    coordinates.append([float(f[0]),float(f[1].strip("\n"))])

pix = 1.126 # pixel size (um)
NN_vectors(coordinates,pix)