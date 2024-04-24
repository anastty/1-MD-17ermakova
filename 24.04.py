def task2():
    from PIL import Image

    holidayotkritka = {
        "8 марта": "8march_card.jpg",
        "23 февраля": "23february_card.jpg"
    }
    holiday = input("Введите название праздника: ")
    if holiday in holidayotkritka:
        cardfile = holidayotkritka[holiday]
        print(f"Открытка к празднику '{holiday}':")

        card_image = Image.open(card_file)
        card_image.show()
    else:
        print("Открытка к этим праздникам не найдена.")

def task1():
    from PIL import Image
    filename  = "otkritka.jpg"
    with Image.open(filename) as img:
        img.load()
        img.crop = img.crop((0,80,200,400))
        img.show()
        img.save("Z:\1-МД-17 алгоритмизация\1-MD-17ermakova")

