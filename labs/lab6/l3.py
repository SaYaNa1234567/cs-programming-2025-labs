x = int(input("Начало: "))
a = int(input("Крнец: "))
if x>a:
    print("Error!")
else:
    prost = []
    for num in range(x, a + 1):
        isProst = True
        if num == 2:
            isProst = True
        elif num % 2 == 0:
            isProst = False
        elif num == 1:
            isProst = False
        else:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    isProst = False
                    break
        if isProst == True:
             prost.append(num)
print(prost)
