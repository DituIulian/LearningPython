waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list, start=1):
    row = f"{index}. {item.capitalize()}"
    print(row)