import random

def rock_paper_scissors_lizard_spock():
    choices = ["камень", "ножницы", "бумага", "ящерица", "спок"]
    rules = {
        "камень": ["ножницы", "ящерица"],
        "ножницы": ["бумага", "ящерица"],
        "бумага": ["камень", "спок"],
        "ящерица": ["бумага", "спок"],
        "спок": ["камень", "ножницы"]
    }
    
    print("Доступные варианты: камень, ножницы, бумага, ящерица, спок")
    user_choice = input("Ваш выбор: ").lower()
    
    comp_choice = random.choice(choices)
    print(f"Компьютер выбрал: {comp_choice}")
    
    if user_choice == comp_choice:
        print("Ничья!")
    elif comp_choice in rules[user_choice]:
        print("Вы победили!")
    else:
        print("Компьютер победил!")

rock_paper_scissors_lizard_spock()
