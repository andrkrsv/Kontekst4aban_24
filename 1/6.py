import math
def hippo(mass, height):
    non_I = (mass**2) + (height**2)
    I = math.sqrt(non_I)
    return I
    
inut = input()
inut2 = input()
print(hippo(float(inut),float(inut2)))