# 3.1 Вводим с клавиатуры десятичное число. Необходимо перевести его  в двоичную систему счисления.

def get_number(input_string):
    '''
    Проверка ввода на число.
    '''
    try:
        num = int(input(input_string))
        return  num
    except(ValueError):
        print('Ошибка ввода! Введите число!')
        return get_number(input_string)

def num_to_2(num):
    num_a = num
    num_b = ''

    while num_a > 0:
        num_b = str(num_a % 2) + num_b
        num_a = num_a // 2

    print(f'Число в двоичной СС: {num_b}')

    num_to_2(get_number('Число в десятичной СС: '))

# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.
# Вводим любую строку текста (на русском).
# Необходимо посчитать количество гласных и согласных букв.

    def get_str(input_string):
        '''
        Проверка ввода на строки.
        '''
        try:
            text = str(input(input_string))
            return text
        except(ValueError):
            print('Ошибка ввода! Введите число!')
            return get_str(input_string)

    def the_latters(text):
        count_glas = 0
        count_soglas = 0
        glas = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
        for i in text:
            if i.isalpha():
                if j in glas:
                    count_glas += 1
                else:
                    count_soglas += 1
        print('Кол-во гласных:', count_glas)
        print('Кол-во согласных:', count_soglas)


# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом

# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами
def Ex_3_4():
    word = input('введите слово: ')
    if len(word) % 2 == 0:
        left = word[0: len(word) // 2]
        right = word[len(word) // 2:0]
        print(right)




# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре
def Ex_3_5():
    stroka = input("Введите любую строку: ")
    let_little = 0
    let_big = 0
    for i in stroka:
        if i.islower():
            let_little += 1
        else:
            if i.isupper():
                let_big += 1
    print(f"Количество маленьких символов: {let_little}")
    print(f"Количество больших символов: {let_big}")
# 3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать - безопасный он или нет. Безопасным считается, если он от 8 символов, есть верхний и нижний регистр. А так же цифры. Можеет, при желании, добавить и спец. символы
# def get_str(input_string):
#     '''
#     Проверка ввода на строки.
#     '''
#     try:
#         text = str(input(input_string))
#         return text
#     except(ValueError):
#         print('Ошибка ввода! Введите число!')
#         return get_str(input_string)
#
# def password(text):
#     if len(text) > 8:
#         if text.isdigit() is False and text.isalpha() is False:
#             if text.islower() is False:
#                 if text.isupper() is False:
#                     print('Пароль надежный!')
#                 else:
#                     password(get_str('Не парвильно! Введите заново -'))
#             else:
#                 password(get_str('Не парвильно! Введите заново -'))
#         else:
#             password(get_str('Не парвильно! Введите заново -'))
#
#     else:
#         password(get_str('Не парвильно! Введите заново'))

# password(get_str('Введите пароль: '))

# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего
sym = input("Введите текст: ")
number_sym = 0
name_sym = 0
for i in sym:
    if sym.count(i) >= number_sym:
        number_sym = sym.count(i)
        name_sym = i
print(f"Самая чаще встречающаяся буква: {name_sym}")

# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "в"
def Ex_3_8():
    print("Нахождение индекс второго символа 'в' ")
    word = input("Введите слово: ")
    if word.count('в') >= 2:
        print(word.find('в', word.find('в') + 1))
    else: print('Второго вхождения нет')

# Test
Ex_3_4()
# Ex_3_5()
# Ex_3_8()
