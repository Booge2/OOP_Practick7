class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, operation):
        if operation == "+":
            return self.add()
        elif operation == "-":
            return self.subtract()
        elif operation == "*":
            return self.multiply()
        elif operation == "/":
            return self.divide()
        else:
            raise ValueError(f"Невідома операція: {operation}")

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("Ділення на нуль!")
        return self.a / self.b


calculator = Calculator(10, 7)
calculator2= Calculator(10, 0)

print(f"Додавання: {calculator('+')}")
print(f"Віднімання: {calculator('-')}")
print(f"Множення: {calculator('*')}")

try:
    print(f"Ділення: {calculator2('/')}")
except ZeroDivisionError as e:
    print(f"Помилка: {e}")

# Завдання 2
import io


class FileSizeDescriptor:

    def __get__(self, instance, owner):
        return self._get_size(instance)

    def __set__(self, instance, value):
        instance._size = value

    def _get_size(self, instance):
        if not instance._size:
            return None
        size_in_bytes = instance._size
        if size_in_bytes < 1024:
            return f"{size_in_bytes} байт"
        elif size_in_bytes < 1048576:
            return f"{size_in_bytes / 1024:.2f} КБ"
        else:
            return f"{size_in_bytes / 1048576:.2f} МБ"


class File:
    size = FileSizeDescriptor()

    def __init__(self, filename):
        self._size = None
        self._filename = filename

        with open(filename, "rb") as f:
            self._size = f.seek(0, io.SEEK_END)


file = File("example.txt")

print(f"Розмір файлу: {file.size}")


# Завдання 4
class User:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Ім'я має бути рядком")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Вік має бути цілим числом")
        if value < 0 and value > 120:
            raise ValueError("Вік має бути в межах від 0 до 120")
        self._age = value


user = User("Іван", 30)

print(f"Ім'я: {user.name}")
print(f"Вік: {user.age}")

try:
    user.age = -10
except AssertionError as e:
    print(f"Помилка: {e}")

try:
    user.age = 150
except AssertionError as e:
    print(f"Помилка: {e}")


# Завдання 3
class Order:

    def __init__(self, order_number, customer_name, items):
        self._order_number = order_number
        self._customer_name = customer_name
        self._items = items

    @property
    def order_number(self):
        return self._order_number

    @property
    def customer_name(self):
        return self._customer_name

    @property
    def items(self):
        return self._items


order = Order(12345, "Іван Петренко", ["Товар 1", "Товар 2"])

print(f"Номер замовлення: {order.order_number}")
print(f"Ім'я клієнта: {order.customer_name}")
print(f"Товари: {order.items}")

try:
    order.order_number = 54321
except AttributeError as e:
    print(f"Помилка: {e}")


# Завдання 5
class Multiplier:

    def __init__(self, multiplier):
        self._multiplier = multiplier

    def __call__(self, number):
        return number * self._multiplier


multiplier = Multiplier(4)

print(multiplier(4))
print(multiplier(10))
