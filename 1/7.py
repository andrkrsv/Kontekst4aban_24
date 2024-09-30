def mass_body(mass, height):
    print(f"Сумма: {mass+height}")
    print(f"Разность: {mass-height}") 
    print(f"Произведение: {mass*height}") 
    print(f"Частное: {mass/height}") 
    return

inut = input().split(' ')
mass_body(float(inut[0]),float(inut[1]))