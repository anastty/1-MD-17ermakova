def_task_1():
countries_capitals = { "Франция": "Париж",
                       "Австрия": "Вена",
                       "Нидерланды": "Амстердам",
                       "Украина": "Киев",
                       "Беларусь": "Минск"}
    print("Страны со своими столицами")
for country,capital in
countries_capitals.items():
    print(f"{country} - {capital}")
    country = "Франция"
if country in countries_capitals:
    print (f"Столица страны {country} - {countries_capitals[country]}")
else:
    print(f"Столицы для этой страны{country} не нашлось.")
sorted_countries_capitals = sorted(countries_capitals.keys())
print("Страны в алфавитном порядке:")
for country in sorted_countries:
    print(f"{country}: {sorted_countries_capitals[country]}")

def_task_2():
letters_value = {"А": 1, "В": 1, "Е": 1, "И": 1, "Н": 1, "О": 1, "Р": 1, "С": 1, "Т": 1
                "Д": 2, "К": 2, "Л": 2, "М": 2, "П": 2, "У": 2,
                "Б": 3, "Г": 3, "Ё": 3, "Ь": 3, "Я": 3,
                "Й": 4, "Ы": 4,
                "Ж": 5, "З": 5, "Х": 5, "Ц": 5, "Ч": 5,
                 "Ш": 8, "Э": 8, "Ю": 8,
                 "Ф": 10, "Щ": 10, "Ъ": 10 }
def calculate_word_value(word):
    value = 0
    for letter in word.upper():
        if letter in letters_value:
            value += letter_values[letter]
        return value
user_word = input("Введите слово: ")
word_value = calculate_word_value[user_word]
   print(f"Цена слова '{user_word}' равна {word_value} очков.")






