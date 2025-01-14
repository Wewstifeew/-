def describe_person(name, age=30):
    print("Имя:", name)
    print("Возраст:", age)

# Пример работы функции
name = input("Введите имя человека: ")
age_input = input("Введите возраст (или оставьте пустым): ")

if age_input:  # Если пользователь ввёл возраст
    age = int(age_input)
    describe_person(name, age)
else:  # Если возраст не введён
    describe_person(name)