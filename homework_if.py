
#Age
age = input("Введите ваш возраст ")
age = int(age)
if age <= 6:
    print("Вы опаздываете в садик")
elif age >=7 and age <= 17:
    print("Вам пора в школу!")
elif age >=18 and age <= 23:
    print("Почему не на парах? В вуз!")
elif  age >=24 and age <= 69:
    print("Вставай с дивана и на работу!")
elif age >= 70:
    print("В России по статистике люди столько не живут!")

#Compare strings

strings1 = input("Введите первую строку ")
strings2 = input("Введите вторую строку ")
strings1 = str(strings1)
strings2 = str(strings2)
len_strings1 = len(strings1)
len_strings2 = len(strings2) #по моему тут какой то китайский код но я что то не как не соображу как написать короче

if strings1 == strings2:
    print("1")
else:
    if len_strings1 > len_strings2:
        print("2")
    else:
        if strings2 == "learn":
            print("3")