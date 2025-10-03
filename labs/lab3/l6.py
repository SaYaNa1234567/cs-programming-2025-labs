x = int(input("Ограничение для числа фибоначчи:"))
a = 0
b = 1
if x >= 0:
    print(a)
while b <= x:
    print(b)
    a, b =b, a+b
