# Из колоды в 52 карты извлекаются случайным образом 4 карты. 
# a) Найти вероятность того, что все карты – крести. 
# б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
import math
# a)

# Всего вариантов извлечения карт:
total_variation = math.factorial(52)/(math.factorial(4)*math.factorial(48))

# Из них сочетания из крести:
x_variation = math.factorial(13)/(math.factorial(4)*math.factorial(9))

# Вероятность:
p = x_variation/total_variation
print(round(p*100,2))

# Ответ: вероятность того, что все карты – крести - 0.26%


# б)

# Всего вариантов извлечения карт:
total_variation = math.factorial(52)/(math.factorial(4)*math.factorial(48))

# Из них сочетания с 1 тузом:
tuz_one_variation = (math.factorial(4)/(math.factorial(1)*math.factorial(3)))*(math.factorial(48)/(math.factorial(3)*math.factorial(45)))


# Из них сочетания с 2 тузами:
tuz_two_variation = (math.factorial(4)/(math.factorial(2)*math.factorial(2)))*(math.factorial(48)/(math.factorial(2)*math.factorial(46)))


# Из них сочетания с 3 тузами:
tuz_three_variation = (math.factorial(4)/(math.factorial(3)*math.factorial(1)))*(math.factorial(48)/(math.factorial(1)*math.factorial(47)))

# Из них сочетания с 4 тузами:
tuz_four_variation = (math.factorial(4)/(math.factorial(4)*math.factorial(0)))

# Вероятность:
p = (tuz_one_variation + tuz_two_variation + tuz_three_variation + tuz_four_variation)/total_variation
print(round(p*100,2))

# Ответ: вероятность, что среди 4-х карт окажется хотя бы один туз - 28,13%