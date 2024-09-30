input()
print(' '.join((lambda a: map(str, [a[0]] + [(a[i-1] + a[i] + a[i+1])/3 for i in range(1, len(a)-1)] + [a[-1]]))(list(map(float,input().split())))))