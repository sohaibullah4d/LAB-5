print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (HOME TASK) ")
print("25-NOV-2018")
print("QUESTION NO:7")

import math
def projectile(initial_velocity,angle):
    angle = math.radians(angle)
    gravity = 9.8
    max_height = (initial_velocity**2)*((math.sin(angle))**2) / (2*gravity)
    time_total = 2*initial_velocity*math.sin(angle) / gravity
    horizontal_range  = (initial_velocity**2)*math.sin((2*angle)) / gravity

    print("\nThe Maximum height reached by the object is: {0:.1f} meters".format(max_height))
    print("The Total time taken by the object is      : {0:.1f} seconds".format(time_total))
    print("The Horizontal Range of the object is      : {0:.1f} meters".format(horizontal_range))
 
