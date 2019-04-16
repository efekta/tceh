# Задача: реализовать игру в загадки
# Программа выводить в консоль текст загадки и ждать ввода пользователя
# Программа после ввода пользователя ответа должна вывести в консоль результат:
# правильный ли ответ дал пользователь
# Загадок должно быть 10, тематика вопросов должна быть по первому занятию
# Дополнительные требования (со звездочкой или сложные, необязательно для выполнения):
# Программа должна в конце игры сказать, сколько ответов дал пользователь:
# сколько из них было верных
# Программа должна не учитывать регистр ответа:
# "Python" и "python" оба должны быть правильным ответом на вопрос "Какой язык мы учим?"
my_dict = { # словарь
    'Какой язык программирования мы изучаем? ' : 'Python',
    'Как обозначается истина?: ' : 'True',
    'Как обозначается ложь?: ' : 'False',
    'Как привести строку в число?: ' : 'int',
    'Как привести целое число в число с плавающей точкой?: ' : 'float',
    'Назовите цикл с пре-условием: ' : 'while',
    'Что вернет выражение len("Hello!")?: ' : '6',
    'Что вернет выражение "Hello"[1]?: ' : 'e',
    'Чему равно утверждение 0 == None ?: ' : 'False',
    'Чему равно утверждение (True or False) and True?: ' : 'True'
}
question_cnt = 0 # счетчик вопросов
answer_cnt = 0 # счетчик ответов

for question in my_dict.keys():
    answer = input(question)
    if answer.lower() == my_dict.get(question).lower():
        print('Верно')
        answer_cnt += 1
        question_cnt += 1
    elif not answer.lower():
        print('Вопрос пропущен')
        question_cnt += 1
    else:
        print('Не верно')
        question_cnt += 1
print("Всего ответов {}, Из них правильных {}".format(question_cnt, answer_cnt))    


# как не учитывать регистр ответа пользователя только в одном случае а в остальных учитывать
questions_to_answers = {
    'Какой язык программирования мы изучаем? ' : ('Python', True),
    'Как обозначается истина?: ' : ('True', False),
    'Как обозначается ложь?: ' : ('False', False),
    'Как привести строку в число?: ' : ('int', True),
    'Как привести целое число в число с плавающей точкой?: ' : ('float', True),
    'Назовите цикл с пре-условием: ' : ('while', True),
    'Что вернет выражение len("Hello!")?: ' : ('6', True),
    'Что вернет выражение "Hello"[1]?: ' : ('e', True),
    'Чему равно утверждение 0 == None ?: ' : ('False', False),
    'Чему равно утверждение (True or False) and True?: ' : ('True', False)
}
question_cnt = 0 # счетчик вопросов
answer_cnt = 0 # счетчик ответов
for question, answer in questions_to_answers.items():
    print('\n')
    print(question)
    user_answer = input()

    is_register_unimportant = answer[1]
    if is_register_unimportant and user_answer.lower() == answer[0].lower():
        print("Верно!")
        answer_cnt += 1
        question_cnt += 1
    elif user_answer == answer[0]:
        print("Верно!")
        answer_cnt += 1
        question_cnt += 1
    elif not user_answer.lower():
        print('Вопрос пропущен')
        question_cnt += 1
    else:
        print("Ответ неверный!")
        question_cnt += 1
print("Всего ответов {}, Из них правильных {}".format(question_cnt, answer_cnt)) 











