
import random
from random import randint
"""Сообщения для игрока в зависимости от результата"""
def phrases(word):
    phrases_negative = ["Дьявол! подбит корабль", "После обстрела мы не досчитались корабля", "SOS!SOS!So...'мы потеряли связь с кораблем'"]
    phrases_positive = ["Точно в цель!", "Вражеское судно пошло ко дну!", "Меткий выстрел, адмирал!"]
    phrases_neutral = ["Косой компьюетер, так и не смог ничего сделать", "Все на месте"]
    phrases_away = ["Молоко!", "Когда закончатся ядра пойдем на абордаж"]

    if word == 'negative': return random.choice(phrases_negative)
    elif word == 'positive': return random.choice(phrases_positive)
    elif word == 'neutral': return random.choice(phrases_neutral)
    elif word == 'away': return random.choice(phrases_away)


"""Создание исходного поля"""
def creating_field(row_m, lines_m):
    field = []
    for r in range(row_m):
        temp_line = []
        for k in range(lines_m):
            temp_line.append(0)
        field.append(temp_line)
    return field


"""Авто расстановка кораблей - для компа """
def accommodation_ships(field_temp,how_many_ships, row_t, lines_t):
    while how_many_ships != 0:
        l = random.randint(0, row_t - 1)
        r = random.randint(0, lines_t - 1)
        if field_temp[l][r] == 0:
            field_temp[l][r] = 1
            how_many_ships -= 1

    return field_temp


"""Ручная расстановка - для игрока"""
def handly_accommodation_ships(field_temp,how_many_ships):#
    print("Давайте расставим корабли")
    while how_many_ships != 0:
        for i in field_temp: print(i)
        try:
            l = int(input("Введите строку :")) - 1
            r = int(input("Введите столбец :")) - 1
            if field_temp[l][r] == 0:
                field_temp[l][r] = 1
                how_many_ships -= 1
        except (IndexError, ValueError):
            print('Ошибка ввода')
    return field_temp
""" Авто стрельба компьютера"""
def aiming(field_temp,lines,row):
    l = random.randint(0, lines - 1)
    r = random.randint(0, row - 1)
    while field_temp[l][r] == "¤" or field_temp[l][r] == "*":
        l = random.randint(0, lines - 1)
        r = random.randint(0, row - 1)
    if field_temp[l][r] == 0:
        field_temp[l][r] = "¤"
        print((phrases('away')))
    elif field_temp[l][r] == 1:
        field_temp[l][r]= "*"
        print((phrases('negative')))
    print("Ваше поле")
    for i in field_temp: print(i)

    return field_temp

#Метод ручного прицеливания (игроком)
def hadly_aiming(field_temp):
    print("")
    field_sneaky = update_field(field_temp) #"""Шифрование кораблей комьютера"""
    print ('Вражеское поле')
    for i in field_sneaky:print(i)
    l = int(input('Введите строку: ')) - 1
    r = int(input('Введите столбец: ')) - 1
    if field_temp[l][r] == 1:
        field_temp[l][r] = "*"
        print(phrases("positive"))
    elif field_temp[l][r] == 0:
        field_temp[l][r] = "~"
        print(phrases("away"))
    else: print(phrases("away"))
    # for i in field_temp: print(i)
    return field_temp

#Метод подсчета кол-ва оставшихся кораблей
def count_ships(field_temp):
    count_ships = 0
    for i in field_temp:
        count_ships += i.count(1)
    return count_ships

def update_field(field):
    field_new = []
    for i in field:
        line = []
        for j in i:
            if j == 0: line.append('#')
            elif j ==1: line.append("#")
            elif j == '*': line.append('*')
            elif j == '~': line.append('~')
        field_new.append(line)
    return field_new

def sea_battle():
    print('Добро пожаловать в морской бой в. 0.2. \n Для начала определимся с размером поля.')
    row = int(input('Введите количество столбцов: '))
    while row < 3 or row > 10:
        row = int(input("Недопустимое значение, введите от 3 до 10: "))
    lines = int(input('Введите количество строк: '))
    while lines < 3 or lines > 10:
        lines = int(input("Недопустимое значение, введите от 3 до 10: "))
    ships = int(input('Введите количество кораблей : '))
    while ships < 1 or ships > row + lines:
        lines = int(input(f"Недопустимое значение, введите от 1 до {row + lines}: "))


    """Ниже 2 строки метода расстановки кораблей, содержащий в себе метод создания поля"""
    field_comp = accommodation_ships(creating_field(row, lines),ships, row, lines)
    field_player = handly_accommodation_ships(creating_field(row, lines), ships)


    """переменные по проверке кол-ва оставшихся кораблей"""
    ships_comp = count_ships(field_comp)
    ships_player = count_ships(field_player)

    """проверка на оставшиеся корабли"""
    while ships_player != 0 or ships_comp != 0:
        field_comp = hadly_aiming(field_comp)
        field_player = aiming(field_player,lines,row)

    if ships_player == 0: winner = "Компьютер"
    else: winner = "Игрок"


    return (f'Выиграл {winner}')

sea_battle()
