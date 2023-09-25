"""#Task-1

sequence = [4, 8, 15, 16, 23, 42]

try:
    # Объединение элементов последовательности  с пробелами
    result = ' '.join(map(str, sequence))
    print(result)
except Exception as error:
    print(f"Произошла ошибка: {error}")


#Task-2
sequence = [4, 8, 15, 16, 23, 42]

try:
    # Мы идем по списку чисел и выводим каждое число на новой строке
    for number in sequence:
        print(number)
except Exception as error:
    print(f"Произошла ошибка: {error}")
    
#Task-3
try:
   
    i= int(input("Enter the first number: "))
    
    # Дадим всем переменым значения
    i2=i+1
    i3=i2+1
    print(i)
    print(i2)
    print(i3)
except ValueError as e:
    print(f"Произошла ошибка: {error}")

    #Task-4
try:
   
    i= int(input("Enter the first number: "))
    
    # Дадим всем переменым значения
    i2=int(input("Enter the first number: "))
    i3=int(input("Enter the first number: "))
    a=i+i2+i3
    print(a)
   
except ValueError as e:
    print(f"Произошла ошибка: {error}")

    #Task-5

try:
    
    edge_len = float(input("Введите длину ребра куба: "))
    
    # (edge_length^3)
    volume = edge_len ** 3
    
    
    surface_area = 6 * (edge_len ** 2)
    
    #  results
    print(f"Volume = {int(volume)}")
    print(f"Total surface area = {int(surface_area)}")
except ValueError as error:
    print(f"Произошла ошибка: {error}")

    #Task-6
try:
    # Ввод данных
    N = int(input("Введите количество школьников: "))
    K = int(input("Введите количество мандаринов: "))
    
    # Вычис количества целых мандаринов на каждого школьника
    целых_мандаринов_на_школьника = K // N
    
    # Вычис остатка мандаринов в корзине
    остаток_мандаринов = K % N
    
    # Вывод результатов
    print(f"Каждый школьник получит {целых_мандаринов_на_школьника} целых мандаринов.")
    print(f"В корзине останется {остаток_мандаринов} целых мандаринов.")
    
except ValueError:
    print("Пожалуйста, введите целые числа для N и K.")
except ZeroDivisionError:
    print("Количество школьников (N) не может быть равным нулю.")

#task-7
try:
   
    i= int(input("Enter the  number: "))
    if 1000 <= i <= 9999:
        a=i//1000
        b=(i%1000)//100
        c=(i%100)//10
        d=i%10
    print(f"The digit in the thousands position is= {int(a)}")
    print(f"The digit in the hundreds position is= {int(b)}")
    print(f"The digit in the tens  position is= {int(c)}")
    print(f"The digit in the position position is= {int(d)}")
   
except ValueError as error:
    print(f"Произошла ошибка: {error}")

#Task-8
try:
    #  Population of the universe
    population = int(input("Enter the population of the universe: "))

    
    if population % 2 == 1:
        
        survivors = (population + 1) // 2
    else:
       
        survivors = population // 2

  
    print("Number of survivors:", survivors)

except ValueError:
    print("Неверный ввод. Пожалуйста, введите допустимое целое число.")
"""
# Task-9
try:
    # Ввод числа от пользователя
    num = int(input("Введите число: "))

    # Выполнение операции левого сдвига (<<)
    result = num << 1

    # Проверка, равен ли результат нулю
    if result == 0:
        print("Предупреждение: Результат << равен нулю.")
    else:
        print(f"Результат << равен {result}")

except ValueError:
    print("Неверный ввод. Пожалуйста, введите целое число.")

# Task-10
try:
    #  Попросить пользователя ввести два числа
    num1 = float(input("Пожалуйста, введите первое число: "))
    num2 = float(input("Пожалуйста, введите второе число: "))

    #  Попросить пользователя выбрать операцию
    operation = input("Пожалуйста, выберите операцию (+, -, *, /): ")

    # Выполнить выбранную операцию и вывести результат
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("Ошибка: Деление на ноль недопустимо.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("Неверная операция. Пожалуйста, выберите из +, -, *, /.")

except ValueError:
    print("Неверный ввод. Пожалуйста, введите действительные числа.")
except Exception as error:
    print(f"Произошла ошибка: {error}")
