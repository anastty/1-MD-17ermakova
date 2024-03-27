days_of_week = ( 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
num_weekend = int(input("Сколько выходных дней вы хотите? "))
your_weekend_days = days_of_week[-num_weekend:]
print("Ваши выходные дни:", ','.join( your_weekend_days ))

your_work_days = days_of_week[:-num_weekend]
print("Ваши рабочие дни:", ','.join( your_work_days ))