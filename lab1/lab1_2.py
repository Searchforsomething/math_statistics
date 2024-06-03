import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

cars_data = pd.read_csv("cars93.csv")
#print(f"data: {cars_data.shape}")
#print(cars_data.head())
print(cars_data['Type'].value_counts(), "\n")
alltypes_horsepower = cars_data['Horsepower'].values.tolist()
alltypes_horsepower.sort()
#print(alltypes_horsepower)

summ = 0
size = len(alltypes_horsepower)
for j in alltypes_horsepower:
    summ += j
average = summ / size
print("Среднее для для всех типов машин :", average)
dispersia = 0
for j in alltypes_horsepower:
    dispersia += j ** 2 - average ** 2
print("Дисперсия для всех типов машин :", dispersia / size)
median = alltypes_horsepower[(size + 1) // 2]
print("Медиана для всех типов машин :", median)
qrange = alltypes_horsepower[size * 3 // 4] - alltypes_horsepower[size // 4]
print("Межквартильный размах мощности для всех типов машин :", qrange, "\n")
pylab.subplot(2, 1, 1)
fig = plt.hist(alltypes_horsepower, histtype='step', cumulative=True, bins=size)
plt.title("Функция распределения мощности для всех типов машин")
alltypes_horsepower_np = np.array(alltypes_horsepower)
pylab.subplot(2, 1, 2)
sns_plot = sns.distplot(alltypes_horsepower_np)
fig = sns_plot.get_figure()
plt.title("Гистограмма мощности для всех типов машин")
plt.show()

cars_type = cars_data['Type'].values.tolist()
unique_types = set(cars_type)
for t in unique_types:
    type1 = cars_data[cars_data['Type'] == t]
    type_horsepower = type1['Horsepower'].values.tolist()
    type_horsepower.sort()
    summ = 0
    size = len(type_horsepower)
    for j in type_horsepower:
        summ += j
    average = summ / size
    print("Среднее для машин с типом", t, ":", average)
    dispersia = 0
    for j in type_horsepower:
        dispersia += j ** 2 - average ** 2
    print("Дисперсия для машин с типом", t, ":", dispersia / size)
    median = type_horsepower[(size + 1) // 2]
    print("Медиана для машин с типом", t, ":", median)
    qrange = type_horsepower[size * 3 // 4] - type_horsepower[size // 4]
    print("Межквартильный размах мощности для машин с типом", t, ":", qrange, "\n")
    pylab.subplot(2, 1, 1)
    fig = plt.hist(type_horsepower, histtype='step', cumulative=True, bins=size)
    title = "Функция распределения мощности для машин типа " + t
    plt.title(title)
    type_horsepower_np = np.array(type_horsepower)
    pylab.subplot(2, 1, 2)
    sns_plot = sns.distplot(type_horsepower_np)
    fig = sns_plot.get_figure()
    title = "Гистограмма мощности для машин типа " + t
    plt.title(title)
    plt.show()
