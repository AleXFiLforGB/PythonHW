#Сообщения для игрока в зависимости от результата
import random
from random import randint


def phrases():
    phrases_negative = []
    phrases_positive = []
    phrases_neutral = []

def creating_field(row_m, lines_m):
    field = []
    for r in range(row_m):
        temp_line = []
        for k in range(lines_m):
            temp_line.append(0)
        field.append(temp_line)
    return field

def accommodation_ships(field_temp,how_many_ships, row_t, lines_t):
    while how_many_ships != 0:
        r = random.randint(0, row_t - 1)
        l = random.randint(0, lines_t - 1)
        if field_temp[r][l] == 0:
            field_temp[r][l] = 1
            how_many_ships -= 1

        return field_temp

def sea_battle():
    print('Добро пожаловать в морской бой в. 0.1. \n Для начала определимся с размером поля.')
    row = int(input('Введите количество столбцов: '))
    while row < 3 or row > 10:
        row = int(input("Недопустимое значение, введите от 3 до 10: "))
    lines = int(input('Введите количество строк: '))
    while lines < 3 or lines > 10:
        lines = int(input("Недопустимое значение, введите от 3 до 10: "))
    ships = int(input('Введите количество кораблей : '))
    while ships < 1 or ships > row:
        lines = int(input(f"Недопустимое значение, введите от 1 до {row}: "))
    field_player = creating_field(row, lines)
    field_comp = creating_field(row, lines)

    field_comp = accommodation_ships(field_comp,ships, row, lines)

    print (field_comp)

sea_battle()
