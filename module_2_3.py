my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
start = 0
while start < len(my_list):
    if my_list[start] == 0:
        start += 1
        continue
    if my_list[start] > 0:
        print(my_list[start])
        start += 1