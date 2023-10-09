money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
budget = money_capital + salary - spend
count_months = 1
budget += salary
while True:
    if budget < spend:
        break
    spend += spend * increase
    budget -= spend
    count_months += 1
    budget += salary

print("Количество месяцев, которое можно протянуть без долгов:", count_months)
