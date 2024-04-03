import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# m2 = (teta ** 2 + teta * (-teta) + (-teta) ** 2) / 3 = teta ** 2 / 3
# teta = (3 * m2) ** 0.5

m = 50
teta = 10
porog = 0.4
sizes = [10, 50, 100, 250, 500, 750, 1000]
percent_all = []
average_all = []

for size in sizes:
    difference = []
    count_porog = 0
    for i in range(m):
        example = np.random.uniform(-teta, teta, size)
        summ = 0
        for j in example:
            summ += j ** 2
        m2 = summ / size
        teta_exp = (3 * m2) ** 0.5
        dif = abs(teta - teta_exp)
        difference.append(dif)
        ex = list(example)
        if dif > porog:
            count_porog += 1
    print("for size", size)
    print("количество выборок с оценкой отличающейся больше чем на поргог:", count_porog)
    percent = 100 * count_porog / m
    print("процент:", percent)
    percent_all.append(percent)
    difference.sort()
    median = difference[(m + 1) // 2]
    summ = 0
    for j in range(m):
        summ += difference[j]
    average = summ / m
    dispersia = 0
    for j in range(m):
        dispersia += difference[j] ** 2 - average ** 2
    average_all.append(average)
    print("Среднее для выборки:", average)
    print("Дисперсия для выборки:", dispersia)
    print("Медиана для для выборки:", median, "\n")
    dif_np = np.array(difference)
    x = "выборка размера " + str(size)
    sns.histplot(dif_np, bins=10).set(title=x)
    plt.show()

plt.plot(sizes, average_all)
plt.xlabel('размеры выборки')
plt.ylabel('среднее')
plt.show()

plt.plot(sizes, percent_all)
plt.xlabel('размеры выборки')
plt.ylabel('процент выборок, где разница превышает порог')
plt.show()