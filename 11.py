def mass_body(mass, height,long):
   b_rast = mass - height
   c_rast = mass - long
   if abs(b_rast) > abs(c_rast):
      print(f"C {abs(c_rast)}")
   else:
      print(f"B {abs(b_rast)}")

inut = input().split(' ')
mass_body(int(inut[0]),int(inut[1]), int(inut[2]))