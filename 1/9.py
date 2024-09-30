def mass_body(mass, height):
    if mass > height:
        print(mass)
    else:
        print(height)

inut = input().split(' ')
mass_body(int(inut[0]),int(inut[1]))