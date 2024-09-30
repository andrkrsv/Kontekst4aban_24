import math

def calculate_oxygen(chelik,dub,topol,days):
    chel_god = chelik*days
    topol_chel = chel_god / topol
    dub_chel = chel_god / dub
    return chel_god,math.ceil(dub_chel),math.ceil(topol_chel)


days = 365
chelik = 0.5
dub = 20
topol = 32

result = calculate_oxygen(chelik,dub,topol,days)

print(f"{result[0]} {result[2]} {result[1]}")