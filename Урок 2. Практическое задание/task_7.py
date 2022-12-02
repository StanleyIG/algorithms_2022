"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""
def func(n, s=0):
    if n == 0:
        return s
    else:
        s += n
        return func(n-1, s)

n = int(input())
right = n * (n + 1) // 2
if func(n) == right:
    print(True)
    print(func(n))
    print(right)




























