class Employee:
    """
    Класс для представления общего сотрудника.
    """

    def __init__(self, name, employee_id):
        """
        Инициализатор (конструктор) класса Employee.

        :param name: Имя сотрудника (тип: str).
        :param employee_id: Идентификационный номер сотрудника (тип: int).
        """
        self.name = name  # Устанавливаем имя сотрудника
        self.employee_id = employee_id  # Устанавливаем ID сотрудника

    def get_info(self):
        """
        Метод для получения базовой информации о сотруднике.

        :return: Строка с информацией о сотруднике (имя и ID).
        """
        return f"Name: {self.name}, ID: {self.employee_id}"


# Пример создания объекта класса Employee
if __name__ == "__main__":
    # Создаем объект сотрудника
    employee = Employee("Alice", 101)

    # Выводим информацию о сотруднике
    print(employee.get_info())
