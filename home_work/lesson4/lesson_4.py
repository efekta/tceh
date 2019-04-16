# Игра "угадай число" (проще)
import random

secret = random.randrange(0, 10)

while True:
    print('компьютер загадывает число от 0 до 10...')
    user_answer = int(input('Угадай, какое число он загадал?: '))
    if user_answer == secret:
        print('УРА! ВЕРНО!')
        break
    else:
        print('Ты не угадал(а) : ( пробуй еще')
        continue