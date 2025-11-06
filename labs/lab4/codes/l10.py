number = int(input("Введите число: "))
if number < 0:
    print("Отрицательные числа не могут быть простыми")
elif number < 2:
    print(f"{number} - не простое число")
prime = True
divisor = None
if number >= 2:
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            prime = False
            divisor = i
            break
    if prime == True:
        print(f"{number} - простое число")
    else:
        print(f"{number} - составное число")
