numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_number = numbers[4]
# print(none_number, type(none_number))
index = 4
modified_array = numbers[:index] + numbers[index+1:]
all_sum = sum(modified_array)
count_numbers = len(numbers)
avg_value = all_sum / count_numbers
# print(modified_array, "\n", all_sum, "\n", count_numbers, "\n", avg_value)
numbers[index] = avg_value
print("Измененный список:", numbers)
