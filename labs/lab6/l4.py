n = int(input())
if n < 2:
    print("Error")
else:
    a = []
    for i in range(n):
        mat1 = list(map(int, input().split()))
        a.append(mat1)
    b = []
    for i in range(n):
        mat2 = list(map(int, input().split()))
        b.append(mat2)
    for i in range(n):
        for j in range(n):
            print(a[i][j] + b[i][j], end=' ')
        print()
