my_list = (2, 3, 5, 8, 7, 2, 5, 9)
dublicates = set([x for x in my_list if my_list.count(x) > 1])

print("Повторяющиеся элементы в списке:", dublicates)