def mass_body(mass, height):
    I = mass/(height**2)
    return I
    
inut = input().split(' ')
print(mass_body(float(inut[0]),float(inut[1])))