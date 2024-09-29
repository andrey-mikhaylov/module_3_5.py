def get_multiplied_digits(n: int) -> int:
    if n < 10:
        return n
    s = str(n)
    return int(s[0]) * get_multiplied_digits(int(s[1:]))


def test():
    result = get_multiplied_digits(40203)
    print(result)
    """ 
    Вывод на консоль:
    24
    """
    pass


def main():
    print(get_multiplied_digits(1))
    print(get_multiplied_digits(9))
    print(get_multiplied_digits(11))
    print(get_multiplied_digits(1111111111111111))
    print(get_multiplied_digits(2222222222222222))
    print(get_multiplied_digits(2222222222200000000000000022222))
    print(get_multiplied_digits(19))
    print(get_multiplied_digits(29))
    print(get_multiplied_digits(99))
    print(get_multiplied_digits(90))


test()
main()



"""
2023/10/11 00:00|Самостоятельная работа по уроку "Рекурсия"
Цель: применить знания о рекурсии в решении задачи.

Задача "Рекурсивное умножение цифр":
Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.

Пункты задачи:
Напишите функцию get_multiplied_digits и параметр number в ней.
Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять срез str_number[1:].
Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
Стек вызовов будет выглядеть следующим образом:
get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

Пример результата выполнения программы:
Исходный код:
result = get_multiplied_digits(40203)
print(result)
Вывод на консоль:
24

Примечания:
При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
Если возникает ошибка, рекомендуется пошагово отладить программу "жучком". Чаще всего ошибка заключается в бесконечной рекурсии или же в неверном обращении по индексу.

Файл с кодом (module_3_5.py) прикрепите к домашнему заданию или пришлите ссылку на ваш GitHub репозиторий с файлом решения.
"""