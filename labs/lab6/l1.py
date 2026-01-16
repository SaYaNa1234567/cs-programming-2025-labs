v, f, t = input("Введите число, единницу измерения и в какую единицу ихмерения хотите(h/m/s) и через пробел: ").split()
v = int(v)
if f == 'h' and t == 'm':
    print(v*60, 'm')
elif f == 'h' and t == 's':
    print(v*3600, 's')
elif f == 'm' and t == 'h':
    print(v//60, 'h')
elif f == 'm' and t == 's':
    print(v*60, 's')
elif f == 's' and t == 'h':
    print(v//3600, 'h')
elif f == 's' and t == 'm':
    print(v//60, 'm')

    



