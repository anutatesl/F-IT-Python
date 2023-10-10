# TODO  Напишите функцию count_letters
def count_letters(text):
    dictionary = {}
    first_elem = 1
    for symbol in text.lower():
        if symbol.isalpha():
            if dictionary.get(symbol) is None:
                dictionary[symbol] = first_elem
            else:
                dictionary[symbol] = dictionary.get(symbol) + 1
    return dictionary


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dictionary):
    sum_symbols = sum(dictionary.values())
    for symbol, value in dictionary.items():
        new_val = value / sum_symbols
        dictionary[symbol] = new_val
    return dictionary


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dictionary_frequency = calculate_frequency(count_letters(main_str))
for key, val in dictionary_frequency.items():
    print(f"{key}: {val:.2f}")
