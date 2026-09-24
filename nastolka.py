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
        break
print('🔴 ОСТОРОЖНО ПРОИЗОШЛА ОШИБКА🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴🔴')
print('🔴ВВЕДИТЕ КОД (подсказка начинается с dfj и в коде 6 букв)🔴')
code=('dfjkar')
while True:

    guess2=input('🔴Введите код🔴 ')

    if guess2!=code:
        print('🔴НЕПРАВИЛЬНО🔴')
    else:
        print('🟢ВЕРНО🟢')
        break

secret_number3=random.randint(1,100)
print('🎲 ИИ загадал число от 1 до 100 отгадай его!!!')

while True:

    guess3=int(input('Введи число! '))

    if guess3 <secret_number3:
        print('Попробуй ещё ИИ загадал число больше!')
    elif guess3>secret_number3:
        print('Попробуй ещё ИИ загадал число меньше!')
    else:
        print('Ура ты угадал!!!')
