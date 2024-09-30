def volnochki(Niggers):
    current_number = 1  
    wave_sise = 1      
    direction = 1    
    num = []
    k=0
    for i in range(2,Niggers):
        if i != 0:
            num.append(i)
    while current_number <= Niggers:
        for i in range(wave_sise):
            if current_number > Niggers:
                break 
            print(current_number, end=" ")
            current_number += 1
        print() 
        try:
            if wave_sise == num[k]:
                k+=1
                direction = -1
            elif wave_sise == 1: 
                direction = 1        
            wave_sise += direction
        except:
            pass
Niggers = int(input())
volnochki(Niggers)
