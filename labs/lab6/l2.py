amount = float(input("Сумма: "))
years = int(input("Годы: "))
if amount < 30000:
    print("Error")
else:
    bonus = (amount // 10000) * 0.3
    if bonus > 5:
        bonus = 5
    if years <= 3:
        rate = 3
    elif years <= 6:
        rate = 5
    else:
        rate = 2
    total = bonus + rate
    current = amount
    for i in range(years):
        current = current + current * (total / 100)
    profit = current - amount
    print(f"{profit:.2f}")
