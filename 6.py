print("MUHAMMAD SOHAIB - 18B-054-CS - SECTION A")
print("LAB NO:5 (HOME TASK) ")
print("25-NOV-2018")
print("QUESTION NO:6")

def first_law(u,a,t):
    v = u + (a*t) #First law
    print("The final velocity is: ",v,"m/s")

def second_law(u,a,t):
    S = u*t +(1/2)*a*(t**2) #Second law
    print("The distance covered is: ",S,"m")

def third_law(u,a,s):
    import math
    V = math.sqrt(u**2)+(2*a*s) #Third law
    print("The final velocity is: ",V,"m/s")

     
    
