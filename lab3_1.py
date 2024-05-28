import numpy as np
import math


def dispersion(sample, mean, size):
    summ = 0
    for i in sample:
        summ += (mean - i) ** 2
    return summ / size


c = 2.0106
mu1 = 2
mu2 = 1

for size in 25, 10000:
    if size == 1000:
        c = 1.96
    amountH0 = 0
    for i in range(1000):

        sample_1 = np.random.normal(2, 1, size)
        sample_2 = np.random.normal(1, 1, size)
        mean1 = np.mean(sample_1)
        mean2 = np.mean(sample_2)
        dispersion_1 = dispersion(sample_1, mean1, size)
        dispersion_2 = dispersion(sample_2, mean2, size)
        h0 = math.sqrt(size ** 2 * (size * 2 - 2) / (size * 2)) * (mean1 - mean2 - 1) / math.sqrt(size * (dispersion_2 + dispersion_1))
        if abs(h0) < c:
            amountH0 += 1
    print(f'при объёме {size} 95-процентный доверительный интервал покрывает реальное значение параметра {amountH0} раз из 1000 ({amountH0 / 1000 * 100}%)')