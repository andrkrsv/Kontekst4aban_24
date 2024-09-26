x = int(input())
k = 0
while x != 1:
    x = x/2 if not x % 2 else 3 * x + 1
    k += 1
print(k)