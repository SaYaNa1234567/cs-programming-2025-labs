n = int(input())
if n < 2:
    print("Error")
else:

    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    
    b = []
    for _ in range(n):
        b.append(list(map(int, input().split())))
    
    for i in range(n):
        for j in range(n):
            print(a[i][j] + b[i][j], end=' ')
        print()
