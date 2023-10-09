# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44  # Мб
number_of_pages = 100
number_of_rows = 50
number_of_characters = 25
buffer = 4  # размер 1ого символа (байт)
inf_volume_byte = inf_volume * 1024**2
count_all_char = number_of_pages * number_of_rows * number_of_characters
weight_book = count_all_char * buffer
print("Количество книг, помещающихся на дискету:", int(inf_volume_byte//weight_book))
