purch = float(input("Введите сумму покупки: "))
if purch < 1000:
    dis = 0
elif 1000 <= purch < 5000:
    dis = 5
elif 5000 <= purch < 10000:
    dis = 10
elif purch >= 10000:
    dis = 15
discount = purch * dis / 100
amount = purch - discount

print("Ваша скидка: ", dis)
print("К оплате: ", amount)
