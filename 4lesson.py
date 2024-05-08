def task1():
def is_divisible_by_3(number):
    return number % 3 == 0

number = int(input("Введите число: "))

if is_divisible_by_3(number):
    print("Число", number, "делится на 3")
else:
    print("Число", number, "не делится на 3")

def task2():
def divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ValueError:
        print("Вы ввели не число")
    except ZeroDivisionError:
        print("Деление на ноль недопустимо")

dividend = 100
divisor = int(input("Введите число: "))

result = divide(dividend, divisor)

if result is not None:
    print("Результат деления:", result)

def task3():
def is_magic_date(date):
    try:
        day, month, year = map(int, date.split("."))
        return day * month == int(str(year)[-2:])
    except ValueError:
        return False

date = input("Введите дату в формате ДД.ММ.ГГГГ: ")

if is_magic_date(date):
    print("Введенная дата является магической")
else:
    print("Введенная дата не является магической")

def task 4():
def is_lucky_ticket(number):
    half_length = len(number) // 2
    first_half = sum(int(digit) for digit in number[:half_length])
    second_half = sum(int(digit) for digit in number[half_length:])
    return first_half == second_half

number = input("Введите номер билета: ")

if is_lucky_ticket(number):
    print("Билет счастливый")
else:
    print("Билет не счастливый")