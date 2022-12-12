#Сообщения для игрока в зависимости от результата
phrases_negative = []
phrases_positive = []
phrases_neutral = []

def creating_field(row_m, lines_m):
    field = []
    for r in row_m:
        for l in lines_m:
            temp_line = []
            temp_line.append(0)
        field.append(temp_line)
    return field

def sea_battle():
    print('Добро пожаловать в морской бой в. 0.1. \n Для начала определимся с размером поля.')
    row = int(input('Введите количество столбцов: '))
        while row <= 3 or row >= 10:
            row = int(input("Недопустимое значение, введите от 3 до 10"))
    lines = int(input('Введите количество строк: '))
        while lines <= 3 or lines >= 10:
            lines = int(input("Недопустимое значение, введите от 3 до 10"))
    ships = int(input('Введите количество кораблей : '))

