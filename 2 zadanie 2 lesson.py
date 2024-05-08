def task1():
password1 = input("Введите пароль: ")
password2 = input("Подтвердите пароль: ")

if password1 == password2:
    print("Пароль принят")
else:
    print("Пароль не принят")


def task2():
number = int(input("Введите номер места: "))

if number <= 20:
    if number % 2 == 0:
        print("Нижнее боковое")
    else:
        print("Верхнее боковое")
elif number <= 40:
    if number % 2 == 0:
        print("Нижнее в купе")
    else:
        print("Верхнее в купе")
else:
    print("Введен некорректный номер места")


def task3():
def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True

year = int(input("Введите год: "))

if is_leap_year(year):
    print("Год", year, "високосный")
else:
    print("Год не високосный")


def task 4()
color1 = input("Введите первый основной цвет: ")
color2 = input("Введите второй основной цвет: ")

if color1 not in ["красный", "синий", "желтый"]:
    print("Неверно введен первый основной цвет")
elif color2 not in ["красный", "синий", "желтый"]:
    print("Неверно введен второй основной цвет")
else:
    if color1 == "красный" and color2 == "синий":
        print("Фиолетовый")
    elif color1 == "красный" and color2 == "желтый":
        print("Оранжевый")
    elif color1 == "синий" and color2 == "желтый":
        print("Зеленый")