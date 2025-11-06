x = input("Введите три числа: ").split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
small = a
if b < small:
    small = b
if c < small:
    small = c
print("Наименьшее: ", small)
