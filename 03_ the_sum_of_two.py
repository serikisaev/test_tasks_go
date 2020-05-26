import random

sub_list = []
with open('input.txt', 'r') as sub_file:
    for line in sub_file:
        sub_list.append(line)
target = int(sub_list[0])
sub_list_2 = set(sub_list[1].split())
sub_list_3 = []
for j in sub_list_2:
    sub_list_3.append(int(j))


def q_sort(mass):
    if len(mass) <= 1:
        return mass
    else:
        first_mass = []
        second_mass = []
        third_mass = []
        a = random.choice(mass)
        for i in mass:
            if i < a:
                first_mass.append(i)
            elif i > a:
                second_mass.append(i)
            else:
                third_mass.append(i)
        return q_sort(first_mass) + third_mass + q_sort(second_mass)


sub_list_4 = q_sort(sub_list_3)
sub_list_5 = []
for k in sub_list_4:
    if target > k:
        sub_list_5.append(k)
    else:
        break
print(sub_list_5)
