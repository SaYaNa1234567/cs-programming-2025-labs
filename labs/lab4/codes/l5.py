password = input("Введите пароль: ")
req = {
        "длина не менее 8 символов": len(password) >= 8,
        "наличие заглавных букв латиницы": any(symb.isupper() for symb in password),
        "наличие строчных букв латиницы": any(symb.islower() for symb in password),
        "наличие чисел": any(symb.isdigit() for symb in password),
        "наличие специальных символов": any(symb in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for symb in password)
    }
failed_req = [req for req, passed in req.items() if not passed]
if not failed_req:
    print("Пароль надежный! Все требования выполнены.")
else:
    print("Пароль ненадежный. Не выполнены следующие требования:")
    for req in failed_req:
        print(f"- {req}")

