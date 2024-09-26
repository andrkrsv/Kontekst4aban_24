k=0
def mass_body(mass, height):
    global k
    for i in range(mass, height+1):
        if i%2!=0: k = k+1
    print(k)


inut = input().split(' ')
mass_body(int(inut[0]),int(inut[1]))