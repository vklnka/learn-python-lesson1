def find_person(name):
    names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
    while names:
        first_name = names.pop()
        if first_name == name:
            print(name, "нашелся")
            break
find_person("Валера")
find_person("Маша")
find_person("Саша")