import random

secret_number=random.randint(1,100)
print('🎲 ИИ загадал число от 1 до 100 отгадай его!!!')

while True:

    guess=int(input('Введи число! '))

    if guess <secret_number:
        print('Попробуй ещё ИИ загадал число больше!')
    elif guess>secret_number:
        print('Попробуй ещё ИИ загадал число меньше!')
    else:
        print('Ура ты угадал!!!')