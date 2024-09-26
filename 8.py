kup = [5000, 1000, 500, 200, 100]

inut = int(input())
result = []
for i in kup:
    a = inut // i
    result.append(a)
    inut -= a * i

print(' '.join(map(str, result)))