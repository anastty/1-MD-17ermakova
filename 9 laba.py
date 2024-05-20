def task_1():
import os
from PIL import Image, ImageFilter

os.makedirs('filtered_images', exist_ok=True)

for filename in os.listdir('images'):
    original_image = Image.open(os.path.join('images', filename))

    filtered_image = original_image.filter(ImageFilter.CONTOUR)

filtered_image.save(os.path.join('filtered_images', f'filtered_{filename}'))

def task_2():
import os
from PIL import Image, ImageFilter

os.makedirs('filtered_images', exist_ok=True)

for filename in os.listdir('images'):
    if filename.endswith('.jpg') or filename.endswith('.png'):
            original_image = Image.open(os.path.join('images', filename))

            filtered_image = original_image.filter(ImageFilter.CONTOUR)

filtered_image.save(os.path.join('filtered_images', f'filtered_{filename}'))

def task_3():
import csv
with open('products.csv', 'r') as f:
    reader = csv.reader(f)

    total_sum = 0

    for row in reader:
        product = row[0]
        quantity = int(row[1])
        price = float(row[2])

        product_cost = quantity * price

        total_sum += product_cost

        print(f'Нужно купить: {product} - {quantity} шт. за {product_cost} руб.')

print(f'Итоговая сумма: {total_sum} руб.')