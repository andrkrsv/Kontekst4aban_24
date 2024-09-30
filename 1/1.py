import math

def calculate_pi(n):
    pi = math.sqrt(12) * (1 - 1/3/3 + 1/5/3**2 - 1/7/3**3 + 1/9/3**4 - 1/11/3**5)
    for i in range (6, n, 2):
        pi += (-1)**(i//2) / (i * 3**(i-1))
    return pi

n = 6
result= calculate_pi(n)
print(result)