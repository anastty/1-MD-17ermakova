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
        img.crop = img.crop((100,200,300,400))
        img.show()
        img.save("Z:\1-МД-17 алгоритмизация\1-MD-17ermakova")

    def task1():
        from PIL import Image, ImageDraw, ImageFont
        a = str(input('Введите имя человека, кому нужно отправить открытку?'))
        image = Image.open("otkritka.jpg")
        font = ImageFont.truetype(font: )
