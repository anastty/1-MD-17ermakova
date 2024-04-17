def task1():
    from PIL import Image

    image = Image.open('cat.png')
    image.show()
    print("Размер изображения:", image.size)
    print("Формат изображения:", image.format)
    print("Цветовая модель:", image.mode)

def  task2():
    from PIL import Image

    orig = Image.open('cat.png')
    small = orig.reduce(3)
    small.save('small_cat.jpg')
    horizontal = orig.transpose(Image.FLIP_LEFT_RIGHT)
    vertical = orig.transpose(Image.FLIP_TOP_BOTTON)
    horizontal.save('horizontal.jpg')
    vertical.save('vertical.jpg')
