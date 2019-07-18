from caesarCryptograph import CaesarCryptograph
from gronsfeldCryptograph import GronsfeldCryptograph
from tritemiusCryptograph import TritemiusCryptographer

print('Привет, юзер! Как ты? Надеюсь у тебя все хорошо! Ну ладно, выбери что ты хочешь сделать! :)')
choose1 = input('Зашифровать сообщение или расшифровать? 1 - зашифровать 2 - расшифровать / любое другое значение\
 - выход--> ')
if choose1 == '1':
    choose2 = input('Выбери свой метод шифровки: 1 - шифр Цезаря 2 - шифр Гронсфельда 3 - шифр Тридемиуса --> ')
    if choose2 == '1':
        text = input('Введите текст, который вы хотите зашифровать, используйте маленькие буквы! ;)\n')
        key = int(input('Введите ключ для зашифровки --> '))
        print(CaesarCryptograph.encrypt(text, key))
    elif choose2 == '2':
        text = input('Введите текст, который вы хотите зашифровать, используйте маленькие буквы! ;)\n')
        key = int(input('Введите ключ для зашифровки --> '))
        print(GronsfeldCryptograph.encrypt(text, key))
    elif choose2 == '3':
        text = input('Введите текст, который вы хотите зашифровать, используйте маленькие буквы! ;)\n')
        print(TritemiusCryptographer.encrypt(text))
elif choose1 == '2':
    choose2 = input('Выбери метод расшифровки сообщения: 1 - шифр Цезаря 2 - шифр Гронсфельда 3 - шифр Тридемиуса --> ')
    if choose2 == '1':
        text = input('Введите текст, который вы хотите расшифровать, используйте маленькие буквы! ;)\n')
        key = int(input('Введите ключ для расшифровать --> '))
        print(CaesarCryptograph.decrypt(text, key))
    elif choose2 == '2':
        text = input('Введите текст, который вы хотите расшифровать, используйте маленькие буквы! ;)\n')
        key = int(input('Введите ключ для расшифровать --> '))
        print(GronsfeldCryptograph.decrypt(text, key))
    elif choose2 == '3':
        text = input('Введите текст, который вы хотите расшифровать, используйте маленькие буквы! ;)\n')
        print(TritemiusCryptographer.decrypt(text))
input('\nВведите любой символ для выхода ')
