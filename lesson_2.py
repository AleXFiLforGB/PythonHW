print ('GB Lesson 2')
# 1) Решить следующую задачу:  генерируем среднее арифметическое последовательности дробных чисел, вводимых с клавиатуры.
# После того, как введем последнее число  - программа выводит среднее арифметическое, максимальное и минимальное значение. (не пользуемся списками и встроенными функциями)
# Количество чисел задаётся в начале работы программы

def Ex_1():
    num = int (input("Введите количество чисел: "))
    maks = 0
    min = 0
    sr = 0
    nums = ""
    for i in range (num):
        temp_digit = float(input("Введите дробное число"))
        if maks < temp_digit: maks = temp_digit
        if min > temp_digit: min = temp_digit
        sr += temp_digit
        nums += str(temp_digit) + " "
    print(f'В последовательности {nums} \n Максимальное число = {maks} \n Минимальное число = {min} \n Средне арифмитическое = {sr}')

# 2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.

def Ex_2():
    num = int(input('Введите число: '))
    for i in range(1, 10):
        print(f'{num} * {i} = {num * i}')

# 3) Решить следующую задачу, проверки знания таблицы умножения.
# Программа выводит 10 примеров и выставляет за 10 правильных ответов - пять, за 9 и 8 - 4 балла, за меньше - три.
# Если пользователь ошибся в каком-то ответе - сообщаем ему об этом
# В итоге выводим количество верных ответов и оценку

def Ex_3():
    from random import randint
    count = 0
    for i in range(10):
        x = randint(1, 9)
        y = randint(1, 9)
        z = int(input(f'Введите ответ на уравнение: {x} * {y} = '))
        if z == x * y: count += 1
        else:
            print('Не верно!')

    if count == 10:mark = 5
    elif count < 10 and count > 7: mark = 4
    else: mark = 3

    print(f'Вы ответили на {count} правильных примеров, ваша оценка {mark} {count}')

# 4) Решить следующую задачу,, выводящиена экран "электронный таймер".
# Ставим таймер - часы, минуты, секунды.
# После отсчета срабатывает будильник

def Ex_4():
    import time

    # hh = int(input("Введите часы: "))
    # mm = int(input("Введите минуты: "))
    # ss = int(input("Введите секунды: "))
    hh = 1
    mm = 12
    ss = 45

    def What_ss(sec):
        while sec != 0:
            # time.sleep(1)
            sec -= 1
            # if sec % 15 == 0: print(f'{hh}:{mm}:{ss}')
        return sec

    def What_mm(min):
        while min != 0:
            What_ss(59)
            min -= 1
        return min

    def What_hh(hour):
        while hour != 0:
            What_mm(59)
            hour -= 1
        return hour

    while ss != 0:
        ss = What_ss(ss)
        if mm > 0 or (mm == 0 and hh > 0):
            while mm != 0:
                mm = What_mm(mm)
                if hh > 0:
                    hh = What_hh(hh)
    print(f'Время вышло! {hh}:{mm}:{ss} ')

# 5) Решить следующую задачу, которая вычисляет наибольший общий делитель двух целых чисел
def Ex_5():
    x = 18
    y = 46


# Test
# Ex_1()
# Ex_2()
# Ex_3()
# Ex_4()
Ex_5()