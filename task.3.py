def isleapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
print (f"Год{year} - високосный")
else:
print("Этот год не високосный")
year = int(input("Введите год:"))
isleapyear(year)