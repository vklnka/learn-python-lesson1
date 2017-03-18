#cycle
cycle = [0,1,2,3,4,5,6,7,8,9]
for a in cycle:
    print(a+1)

#cycle2
word = input("Введите слово ")
for a in word:
    print(a)

#mark

def count_mark_school():
    mark_school = 0
    mark_school = mark_all/amount_class
    print(mark_school)

mark_all = 0 #сумма всех оценок
amount_class = 0 #число оценок
school = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores': [5,3,5,5,5]}, {'school_class': '4v', 'scores': [1,5,5,2,3]}]
for school_class in school: #запускаем цикл который вытащит словари из списка
    class_mark = 0
    for mark in school_class['scores']: #запускаем цикл который вытащит значения оценок по одному из словаря по ключу 'scores'
        mark_all += mark
        class_mark += mark
    class_quantity = len(school_class['scores']) #тут мы получили сколько оценок в отделном классе
    amount_class += class_quantity #тут мы в цикле добавляем сколько всего оценок
    print('в классе', school_class['school_class'], 'средняя оценка', class_mark/class_quantity)
print('Средняя оценка в школе', count_mark_school())