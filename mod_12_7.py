per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Сумма вклада")
valuesList = list(per_cent.values())
result = [num * float(money) * 0.01 for num in valuesList]
print("Money =", money)
print("Deposit =",result)
max_profit = max(result)
print("Максимальная сумма, которую вы можете заработать -", max_profit)
