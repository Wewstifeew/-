def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Пример работы функции
number = int(input("Введите число для проверки на простоту: "))
if is_prime(number):
    print("Число", number, "является простым.")
else:
    print("Число", number, "не является простым.")
