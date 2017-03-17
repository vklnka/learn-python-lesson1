#get_answer()

def ask_user():
    while True:
        user_say = input("Спросите что нибуть? ")
        if user_say == "Пока":
            print("Ну пока")
            break
        else:
            print("Я отвечаю на ваш вопрос что нибуть")
ask_user()