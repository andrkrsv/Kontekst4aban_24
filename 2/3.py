def tabliochka(row, col):
    print("    |", end="")
    for j in range(1, col + 1):
        print(f"{j:4}", end="")
    print()
    print("   "+ "-" * (col * 4 + 2))
    for i in range(1, row + 1):
        print(f"{i:4}|", end="") 
        for j in range(1, col + 1):
            print(f"{i * j:4}", end="") 
        print()

row, col = map(int, input().split())
tabliochka(row, col)
