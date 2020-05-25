def unique_number(file):
    sub_list = []
    sub_list_2 = []

    with open(file, 'r') as sub_file:
        for line in sub_file:
            sub_list.append(int(line))

    for i in sub_list:
        if sub_list.count(i) == 1:
            sub_list_2.append(i)

    with open('input-201.a.txt', 'w') as sub_file_2:
        for i in sub_list_2:
            print(i, file=sub_file_2)


unique_number('input-201.txt')
