seatnumber = int(input("Укажите ваш номер места в вагоне:"))
if seatnumber % 2 == 0
    seattype = "нижнее"
else:
    seattype = "верхнее"
if seatnumber <= 50
    placetype = "купе"
    else:
    placetype = "боковое"
    print(f"Место{seatnumber} - {seattype}место,{placetype}")
