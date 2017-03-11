question = input()
def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    question = str.lower(question)
    return answers.get(question)
print(get_answer(question))
