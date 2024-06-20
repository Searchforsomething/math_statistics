import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


durations = np.array([235, 173, 202, 201, 295, 324, 222, 234, 174, 229,
                      201, 191, 163, 238, 195, 216, 234, 224, 203, 223,
                      174, 258, 158, 238, 172, 145, 252, 263, 222, 219])


sample_mean = np.mean(durations)
sample_var = np.var(durations, ddof=0)  # Смещенная дисперсия
sample_unbiased_var = np.var(durations, ddof=1)  # Несмещенная дисперсия
sample_median = np.median(durations)
X_1 = np.min(durations)
X_n = np.max(durations)
print("Вариационный ряд:", np.sort(durations))
print("Выборочное среднее:", sample_mean)
print("Смещенная дисперсия:", sample_var)
print("Несмещенная дисперсия:", sample_unbiased_var)
print("Медиана:", sample_median)
print("Минимальное значение (X_1):", X_1)
print("Максимальное значение (X_n):", X_n)

# Гистограмма
plt.hist(durations, bins='auto', alpha=0.7, rwidth=0.85)
plt.title('Histogram of Song Durations')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.show()

# Box-plot
plt.boxplot(durations, vert=False)
plt.title('Box plot of Song Durations')
plt.xlabel('Duration (seconds)')
plt.show()

def ecdf(data):
    """Вычисляет значения ECDF для одномерного массива данных."""
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1) / n
    return x, y

x, y = ecdf(durations)
plt.step(x, y, where='post')
plt.title('Empirical Cumulative Distribution Function')
plt.xlabel('Duration (seconds)')
plt.ylabel('ECDF')
plt.grid(True)
plt.show()

a_hat = np.min(durations)
b_hat = np.max(durations)

print("Оценка a:", a_hat)
print("Оценка b:", b_hat)

confidence_level = 0.95
degrees_freedom = len(durations) - 1
sample_mean = np.mean(durations)
sample_standard_error = stats.sem(durations)

confidence_interval_mean = stats.t.interval(confidence_level, degrees_freedom, sample_mean, sample_standard_error)

print("Доверительный интервал для математического ожидания (уровень 0.95):", confidence_interval_mean)

sample_variance = np.var(durations, ddof=1)
chi2_lower = stats.chi2.ppf((1 - confidence_level) / 2, degrees_freedom)
chi2_upper = stats.chi2.ppf(1 - (1 - confidence_level) / 2, degrees_freedom)

confidence_interval_variance = (degrees_freedom * sample_variance / chi2_upper, degrees_freedom * sample_variance / chi2_lower)

print("Доверительный интервал для дисперсии (уровень 0.95):", confidence_interval_variance)

other_durations = np.array([161, 186, 205, 294, 294, 193, 366, 296, 238, 173,
                            230, 246, 310, 220, 125, 270, 142, 187, 326, 268,
                            298, 138, 312, 304, 360, 217, 81, 307, 178, 272])

t_stat, p_val = stats.ttest_ind(durations, other_durations)

print("t-Statistic:", t_stat)
print("p-value:", p_val)

if p_val < 0.05:
    print("Две выборки зависимы")
else:
    print("Две выборки независимы")

