fruits = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
result = {}
for fruit in fruits:
    first_letter = fruit[0]
    if first_letter not in result:
        result[first_letter] = []
    result[first_letter].append(fruit)
print(result)
