# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=","):
    list1_ = first_group.split(separator)
    list2_ = second_group.split(separator)
    intersection_set = list(set(list1_).intersection(list2_))
    intersection_set.sort()
    return intersection_set


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator="|"))
