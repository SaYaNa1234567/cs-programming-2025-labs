while True:
    try:
        x = int(input("Введите число от 1 до 9:"))
        if x >= 1 and x <= 9:
            break
        else:
            print("Ошибка")
    except error:
        print("Число должно быть в диапазоне от 1 до 9!")
for i in range(1,11):
    res = x * i
    print(f"{x} * {i} = {res}")

