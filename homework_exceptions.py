
def ask_user():
    try:
        while True:
            user_say = input("Спросите что нибуть? ")
            if user_say == "Пока":
                print("Ну пока")
                break
            else:
                print("Я отвечаю на ваш вопрос что нибуть")
    except (ValueError, TypeError, IndexError, KeyError):
        print(" Пока!")
        pass


ask_user()