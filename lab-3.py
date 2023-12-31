#Task-1
"""

# Ввод четырехзначного числа
number = int(input("Введите четырехзначное число: "))

# Разбиваем число на отдельные цифры
digit_1 = number // 1000
digit_2 = (number // 100) % 10
digit_3 = (number // 10) % 10
digit_4 = number % 10

# Проверяем условие
if digit_1 + digit_4 == digit_2 - digit_3:
    print("YES")
else:
    print("NO")
"""
#Task-2
"""

# Ввод возраста пользователя
age = int(input("Введите возраст пользователя: "))

# Проверка возраста и вывод соответствующего сообщения
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
    """
#Task-3
"""
# Ввод трех чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Проверка, являются ли они последовательными членами арифметической прогрессии
if b - a == c - b:
    print("YES")
else:
    print("NO")


"""

#Task-4

"""# Ввод координат первой клетки
x1 = int(input("Введите номер столбца для первой клетки (от 1 до 8): "))
y1 = int(input("Введите номер строки для первой клетки (от 1 до 8): "))

# Ввод координат второй клетки
x2 = int(input("Введите номер столбца для второй клетки (от 1 до 8): "))
y2 = int(input("Введите номер строки для второй клетки (от 1 до 8): "))

# Проверка, может ли ладья переместиться из первой клетки во вторую
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")"""


#Task-5
"""
# Ввод координат первой клетки
x1 = int(input("Введите номер столбца для первой клетки (от 1 до 8): "))
y1 = int(input("Введите номер строки для первой клетки (от 1 до 8): "))

# Ввод координат второй клетки
x2 = int(input("Введите номер столбца для второй клетки (от 1 до 8): "))
y2 = int(input("Введите номер строки для второй клетки (от 1 до 8): "))

# Проверка, может ли король переместиться из первой клетки во вторую
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")

"""
#Task-6
"""
# Ввод трех различных целых чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Найдем среднее из трех чисел, сначала отсортировав их в порядке возрастания
sorted_numbers = sorted([a, b, c])
average = sorted_numbers[1]

# Выводим среднее число
print(average)
"""

#Task-7
"""
# Ввод порядкового номера месяца
month = int(input("Введите порядковый номер месяца (от 1 до 12): "))

# Определение количества дней в месяце с использованием словаря
days_in_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Вывод количества дней в месяце
if month in days_in_month:
    print(days_in_month[month])
else:
    print("Введен неверный номер месяца.")

"""
#Task-8
"""
# Ввод веса боксера
weight = int(input("Введите вес боксера (целое число): "))

# Определение категории веса и вывод результата
if weight <= 60:
    print("Light weight")
elif weight <= 64:
    print("First welterweight")
elif weight <= 69:
    print("Welterweight")
else:
    print("Боксер не подходит ни в одну из категорий.")

"""
#Task-9
"""
# Ввод пароля
password = input("Введите пароль: ")

# Ввод подтверждения пароля
confirmation = input("Подтвердите пароль: ")

# Сравнение пароля и его подтверждения и вывод результата
if password == confirmation:
    print("Password accepted")
else:
    print("Password not accepted")
"""
#Task-10
"""
# Ввод числа
number = int(input("Введите число: "))

# Проверка, является ли число четным или нечетным, и вывод результата
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
"""
#Task-11
"""
# Ввод двух различных целых чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Определение наименьшего числа и вывод результата
if a < b:
    print(a)
else:
    print(b)
"""
#Task-12
"""
# Ввод возраста пользователя
age = int(input("Введите возраст: "))

# Определение возрастной группы и вывод результата
if age <= 13:
    print("childhood")
elif 14 <= age <= 24:
    print("youth")
elif 25 <= age <= 59:
    print("maturity")
else:
    print("old age")
"""
#Task-13

# Ввод длин трех сторон треугольника
a = int(input("Введите длину первой стороны: "))
b = int(input("Введите длину второй стороны: "))
c = int(input("Введите длину третьей стороны: "))

# Проверка типа треугольника и вывод результата
if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Versatile")

