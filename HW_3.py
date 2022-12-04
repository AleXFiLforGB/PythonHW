# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

# 3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

def Ex3_11():
    str = input("Введите дробное число: ")
    str = str.replace(',', '.')
    if len(str) >= 3:
        if str.count(".") == 1 and (str.find(".") != 0 or str.find(".") != len(str)-1):
            point = str.find(".")
            if str[0:point].isdigit() and str[point + 1:].isdigit():
                return print(f'{str} является дробным числом')
    return print(f'{str} не является дробным числом')

# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку
# между первой и последней буквой "о" из исходной строки.
# Если она только одна или её нет - то сообщить, что буква "о" - одна или не встречается.

def Ex3_12():
    str = input("Введите строку с 2-мя и более буквами о: ")
    str = str.replace("o", "о")
    if str.count("о") <= 1: print('буква "о" - одна или не встречается')
    else: print(str[str.find("о"):str.rfind("о")])

# Test
# Ex3_11()
# Ex3_12()