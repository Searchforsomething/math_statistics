import numpy as np
from scipy.stats import norm

def poisson_second_moment_confidence_interval(lmbda, n, alpha):
    # Генерируем выборку
    sample = np.random.poisson(lmbda, n)
    # Оцениваем второй момент
    second_moment_estimate = np.mean(sample ** 2)
    # Квантиль нормального распределения
    z_alpha_2 = norm.ppf(1 - alpha / 2)
    # Асимптотический доверительный интервал
    interval_half_width = z_alpha_2 * np.sqrt((lmbda + lmbda**2) / n)
    lower_bound = second_moment_estimate - interval_half_width
    upper_bound = second_moment_estimate + interval_half_width
    return lower_bound, upper_bound

def coverage_probability(lmbda, n, alpha, num_samples):
    covered = 0
    for _ in range(num_samples):
        lower, upper = poisson_second_moment_confidence_interval(lmbda, n, alpha)
        if lower <= lmbda + lmbda**2 <= upper:
            covered += 1
    return covered / num_samples

# Параметры эксперимента
lmbda = 1
alpha = 0.05
num_samples = 1000

# Для выборки размером 25
n = 25
coverage_prob_25 = coverage_probability(lmbda, n, alpha, num_samples)
print(f"Вероятность покрытия для выборки размером {n}: {coverage_prob_25:.4f}")

# Для выборки размером 10000
n = 10000
coverage_prob_10000 = coverage_probability(lmbda, n, alpha, num_samples)
print(f"Вероятность покрытия для выборки размером {n}: {coverage_prob_10000:.4f}")
