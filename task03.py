# В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. 
# Какова вероятность того, что все извлеченные детали окрашены?


import math

# Всего вариантов извлечения:
total_variation = math.factorial(15)/(math.factorial(3)*math.factorial(12))

# Из них окрашенных вариантов:
colored_variation = math.factorial(9)/(math.factorial(3)*math.factorial(6))

# Тогрда вероятность равна:
p = colored_variation/total_variation
print(round(p*100,2))

# Ответ: вероятность того, что все извлеченные детали окрашены - 18.48%