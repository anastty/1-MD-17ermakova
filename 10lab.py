def task_1():
    import json

with open('products json', 'r') as f:
    products = json.load(f)
for product in products:
    print('Название:', product['name'])
    print('Цена:', product['price'])
    print('Bec:', product['weight '])
    if product['available']:
        print('В наличии')
    else:
        print('Нет в наличии!')
    print()

def task_2():
 import json
with open('products.json', 'r') as f:
    products = json.load(f)

name = input("Введите назввание продукта: ")
price = int(input("Введите цену продукта: ") )
weight = int(input("Введите вес продукта: " ) )
available = input("В наличии ли продукт (да/нет): ") == "да"

products.append({
        "name": name,
        "price": price,
        "weight": weight,
        "available": available })

with open('products. json', 'w') as f:
        json.dump(products, f)

for product in products:
    print('Название:', product['name'])
    print('Цена:', product ['price'])
    print('Bec:', product['weight'])
    if product['available']:
        print('B наличии')
    else:
        print('Нет в наличии!')
    print()

def task_3():
with open('en-ru.txt', 'r') as f_in:
    en_ru = {}
    for line in f_in:
        en, ru = line.strip().split(' - ')

        en_ru[ru] = en
ru_en = {}
for ru, en in en_ru.items():
        if en not in ru_en:
            ru_en[en] = [ru]
        else:
            ru_en[en].append(ru)
with open('ru-en.txt', 'w') as f_out:
    for en, ru_list in
sorted(ru_en.items()):
        for ru in ru list:
            f_out.write(f'{ru} - {en}\n')