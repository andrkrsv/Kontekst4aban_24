def get_excel(n):
    result = []
    while n > 0:
        n -= 1
        remainder = n % 26
        result.append(chr(remainder + ord('A')))
        n //= 26
    return ''.join(reversed(result))

n = int(input().strip())
column = get_excel(n)
print(column)
