value = float(input("Количество:"))
orig = input("Часы/минуты(h/m):")

if orig == 'h':
    print(value * 60, "m")
elif orig == 'm':
    print(value / 60, "h")
else:
    print(value)
