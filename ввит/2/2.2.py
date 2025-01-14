def greet(name):
    print("Привет,", name)

def square(number):
    return number * number

def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y

Пример работы
user_name = input("Введите своё имя: ")
greet(user_name)

number = int(input("Введите число для возведения в квадрат: "))
print("Квадрат числа:", square(number))

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
print("Большее из двух чисел:", max_of_two(x, y))