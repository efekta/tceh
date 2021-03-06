# *Сложный вариант:
# Задача: необходимо реализовать игру в пятнашки.
# Задача про пятнашки действительно непростая, но очень интересная.
#
# **Требования:
# 1. Игра пятнашки: https://ru.wikipedia.org/wiki/%D0%98%D0%B3%D1%80%D0%B0_%D0%B2_15
# 2. Поле состоит из клеток от 1 до 15 и пустой клетки
# 3. Управление ведется кнопками "wasd", двигается пустая клетка
# 4. В начале игры поле перемешено в случайном порядке
# 5. Пользователь не должен соверашть непозволительные шаги.
# Например, из-за ограничений рамки поля. Ему должно показываться сообщение о том,
# что он пытается совершить непозволительный ход
# 6. Пользователю дожно быть видно поле. Оно представляет собой матрицу 4 на 4.
# Пустую клекту обозначаем как x. При каждом действии пользователя поле рисуется еще раз - ниже в консоли
# 7. Игра заканчивается, когда все клетки стоят по-порядку, а пустая клетка - последняя.
# В конце игры пользователю показывается, сколько ходов он совершил
# 8. Выход из игры происходит при помощи KeyboardInterrupt. Исключение должно быть обработано.
# Пользователю должна быть выведена фраза "shutting down"
#
# **Дополнительно:
# 1. Обратите внимание, что не любое поле оставляет возможность закончить игру,
# необходимо придумать корректный алгоритм генерации взамен простого перемешивания
# 2. Тесты, которые приложены к работе должны проходить
# 3. Вам необходимо посмотреть, как работают самописные тесты, которые приложены к работе
#
# **Прохождение тестов:
# 1. Создаем папку game_code
# 2. В ней создаем файл game.py
# 3. Рядом должен лежать мой файл tests.py
# 4. Вызываем python3 tests.py