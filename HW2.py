# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3
def Ex_1():
    x = int(input("Введите значение Х: "))
    y = int(input("Введите значение У: "))
    count = 0
    if x > y:
        x, y = y, x
    for i in range(x, y + 1):
        if i % 2 == 0 and i % 3 == 0 and i != 0:
            count += 1
    print(count)

# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
def Ex_2():
    length = int(input('Введите кол-во чисел: '))
    while length < 1:
        length = int(input('Некорректный ввод.Введите кол-во чисел: '))
    values = []
    for i in range(length): values.append(int(input('Введите число: ')))
    values.sort()
    if length == 1: print(f'Число всего одно и его значение {values[0]}')
    else: print(f'Максимальное значение {values[length - 1]}, второе максимально число {values[length - 2]}')

# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

def Ex_3():
    salary = int(input('Сейчас расчитаем вашу зарплатку в бумажках, какая она у Вас?'))
    C25 = salary // 25
    C10 = (salary - (C25 * 25)) // 10
    C3 = (salary - (C25 * 25) - (C10 * 10)) // 3
    C1 = salary - (C25 * 25) - (C10 * 10) - (C3 * 3)

    print(f"""
    Следующую зарплату эквивалентом {salary} рублей вы получите бумажками в количестве:
    - {C25} шт 25-руб;
    - {C10} шт 10-руб;
    - {C3} шт 3-руб;
    - {C1} шт 1-руб.
    """)

# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет
def Ex_4():
    word = input('А сейчас проверим ваше число на упорядоченность по возрастанию, кстати, где оно? \n Введите число:')
    increase = True
    while len(word) <= 1:
        word = (input('Я разве не сказал, нужно многозначное число. \n Введите многозначное число'))
    i1 = 1
    i2 = 0
    for i in word[1: len(word)]:
        if word[i1] < word[i2]:
            increase = False
            continue
        i1 += 1
        i2 += 1
    if increase == True: print('Да, цифры упорядочены по возрастанию')
    else: print('Нет, цифры не упорядочены по возрастанию')


#Test
# Ex_1()
# Ex_2()
# Ex_3()
# Ex_4()