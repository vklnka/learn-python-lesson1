names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
while names:
    first_name = names.pop()
    if first_name == "Валера":
        print("Валера нашелся")
        break