# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint as ran

def Ex_4_1():
    LS = []
    res = 0
    nums = int(input("Введите количество чисел: "))
    for i in range(nums):
        LS.append(ran(1,10))
    print(f"Поищем сумму нечетных элементов списка \n {LS}")
    for k in range(len(LS)):
        if k % 2 != 0: res += LS[k]
    print(f'И результат суммы равен {res}')

# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
def Ex_4_2():
    A = int(input('Введите количество строк: '))
    B = int(input('Введите количество столбцов: '))
    a = []
    for i in range(A):
        b = []
        for k in range(B):
            b.append(ran(1,10))
        a.append(b)

    for element in a:
        mid_value = 0
        for n in element: mid_value += n
        print(f'{element} среднее значение строки {mid_value//B}')

# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
def EX_4_3():
    nums = []
    for i in range(10):
        nums.append(ran(1,100))
    print(nums)

    for i in range(len(nums)):
        low = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[low]: low = j
        nums[i], nums[j] = nums[j], nums[i]
        print(nums)

# Ex_4_1()
Ex_4_2()
# EX_4_3()