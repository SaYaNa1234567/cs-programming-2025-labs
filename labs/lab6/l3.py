a = int(input("Диапозон начало:"))
b = int(input("Диапозон конец:"))
if a > b:
    print("Error!")
else:
    primes = []
    for num in range(a, b + 1):
        if num < 2:
            continue 
        is_prime = True
        if num == 2:
            is_prime = True
        elif num % 2 == 0:
            is_prime = False
        else:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(num)
    if primes:
        for p in primes:
            print(p, end=" ")
    else:
        print("Error!")
