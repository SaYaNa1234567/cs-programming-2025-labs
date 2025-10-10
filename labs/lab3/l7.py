x = input("Напишите слово: ")
res = ""
for i in range(len(x)):
    res += x[i] + str(i + 1)
print(res)
    
