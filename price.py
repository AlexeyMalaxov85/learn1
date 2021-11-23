#Задание 1 Функции
#1) Создайте функцию get_summ(one, two, delimiter='&'), которая принимает два
#   параметра, приводит их к строке и отдает объединенными через разделитель delimiter
#2) Вызовите функцию, передав в нее два аргумента "Learn" и "python", положите результат в
#   переменную и выведите ее значение на экран
#3) Сделайте так, чтобы результирующая строка выводилась заглавными буквами

def get_sum(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    delimiter = str('&')
    return str(one + delimiter + two)

summ = get_sum('Learn', 'python').upper()
print(summ)


def format_price(price):
    price = float(price)
    return f'Цена: + {price} + руб.'

a = format_price(56.24)
print(a)
