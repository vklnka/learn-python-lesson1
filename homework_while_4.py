def get_answer():
    print(ask_user())

def ask_user():
    while True:
        user_say = input("Спросите что нибуть? ")
        if user_say == "Пока":
            print("Ну пока")
            break
        else:
            print("Я отвечаю на ваш вопрос что нибуть")

get_answer()