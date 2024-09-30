def rle_compress(s):
    compressed = [] 
    n = len(s)
    i = 0
    while i < n:
        count = 1
        while i + 1 < n and s[i] == s[i + 1]:
            count += 1  
            i += 1
        if count > 1:
            compressed.append(f"{s[i]}{count}")
        else:
            compressed.append(s[i])
        i += 1  
    return ''.join(compressed)  
input_string = input().strip() 
compressed_string = rle_compress(input_string)
print(compressed_string)
