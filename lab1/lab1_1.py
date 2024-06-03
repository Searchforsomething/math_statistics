import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pylab

low = 0
high = 1000
size = 100

average = []
dispersia = []
median = []
nFx_2 = []
nFx_n = []

for i in range(500):
    example = list(np.round(np.random.uniform(low, high, size)))
    summ = 0
    for j in range(100):
        summ += example[j]
    average_x = summ / size
    average.append(average_x)
    dispersia_x = 0
    for j in range(size):
        dispersia_x += example[j] ** 2 - average_x ** 2
    dispersia.append(dispersia_x / size)
    example.sort()
    nFx_2_x = (example[1] - low) / (high - low) * size
    nFx_2.append(nFx_2_x)
    nFx_n_x = (example[-1] - low) / (high - low) * size
    nFx_n.append(nFx_n_x)
    median_x = example[size // 2]
    median.append(median_x)

average.sort()
median.sort()
dispersia.sort()
nFx_2.sort()
nFx_n.sort()

average_np = np.array(average)
median_np = np.array(median)
dispersia_np = np.array(dispersia)
nFx_2_np = np.array(nFx_2)
nFx_n_np = np.array(nFx_n)

pylab.subplot(2, 2, 1)
sns_plot = sns.distplot(average_np)
fig = sns_plot.get_figure()
plt.title("Среднее")

pylab.subplot(2, 2, 2)
sns_plot = sns.distplot(median_np)
fig = sns_plot.get_figure()
plt.title("Медиана")

pylab.subplot(2, 2, 3)
sns_plot = sns.distplot(dispersia_np)
fig = sns_plot.get_figure()
plt.title("Дисперсия")
plt.show()

pylab.subplot(2, 1, 1)
sns_plot = sns.distplot(nFx_2_np)
fig = sns_plot.get_figure()
plt.title("n*F(x(2))")

pylab.subplot(2, 1, 2)
gamma_example_np = np.random.gamma(2, 1, 100)
sns_plot = sns.distplot(gamma_example_np)
fig = sns_plot.get_figure()
plt.title("Гамма-распределение с параметрами 1, 1")
plt.show()

pylab.subplot(2, 1, 1)
sns_plot = sns.distplot(nFx_n_np)
fig = sns_plot.get_figure()
plt.title("n*F(x(n))")

pylab.subplot(2, 1, 2)
gamma_example_np = np.random.gamma(1, 1, 100)
sns_plot = sns.distplot(gamma_example_np)
fig = sns_plot.get_figure()
plt.title("Гамма-распределение с параметрами 1, 1")
plt.show()
