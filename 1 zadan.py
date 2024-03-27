numbers = ( 1, 2, 3, 4, 5)
user_number = int (input("Введите любое число: "))
if user_number in numbers:
    print("Поздравляю, вы угадали число!")
else:
     print("Нет такого числа!")

print("Исходный список:", numbers)
print("Число пользователя:", user_number)
