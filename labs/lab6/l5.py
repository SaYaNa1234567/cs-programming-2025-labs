text = input()
cleaned = ""
for c in text:
    if c.isalpha():
        cleaned += c.lower()
if cleaned == cleaned[::-1]:
    print("Да")
else:
    print("Нет")
