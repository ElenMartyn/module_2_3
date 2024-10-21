my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_list = 0
while number_list < len(my_list):
    number = my_list[number_list]
    if number < 0:
        break
    if number > 0:
        print(number)
    number_list += 1

