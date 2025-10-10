x = int(input("Введите число от 1 до 9:"))
if x < 1 or x > 9:
    print("Ошибка.")
    x = int(input("Введите число от 1 до 9:"))
for i in range(1,11):
    res = x * i
    print(f"{x} * {i} = {res}")

