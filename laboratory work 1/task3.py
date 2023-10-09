list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
count_all_players = len(list_players)
count_players_on_team = count_all_players / 2
first_team = list_players[:int(count_players_on_team)]
second_team = list_players[int(count_players_on_team):]
print(first_team)
print(second_team)
