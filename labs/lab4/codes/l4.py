number = input()
last_num = int(number[-1])
sum_num = sum(int(x) for x in number)
if last_num % 2 == 0 and sum_num % 3 == 0:
    print(f"Число {number} делится на 6")
else:
    print(f"Число {number} не делится на 6")
    
