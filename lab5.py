import pandas as pd
import numpy as np
from scipy.stats import t, f


# Загрузка данных
data = pd.read_csv('song_data.csv')

# Извлечение переменных
X = data[['song_duration_ms', 'danceability', 'energy']].values
y = data['song_popularity'].values

# Добавление столбца единиц для свободного коэффициента
X = np.hstack((np.ones((X.shape[0], 1)), X))

# Расчет коэффициентов
X_transpose = X.T
beta = np.linalg.inv(X_transpose @ X) @ X_transpose @ y
print("Оценки коэффициентов (бета):", beta)


n = len(y)
p = X.shape[1]
e = y - X @ beta
residual_variance = (e.T @ e) / (n - p)
print("Остаточная дисперсия:", residual_variance)

SS_res = e.T @ e
SS_tot = ((y - np.mean(y)) ** 2).sum()
R2 = 1 - SS_res / SS_tot
print("Коэффициент детерминации (R^2):", R2)


alpha = 0.05
t_value = t.ppf(1 - alpha/2, n - p)
beta_var = residual_variance * np.linalg.inv(X_transpose @ X).diagonal()

confidence_intervals = np.vstack((beta - t_value * np.sqrt(beta_var), beta + t_value * np.sqrt(beta_var))).T
print("Доверительные интервалы для коэффициентов:")
print(confidence_intervals)

beta_3 = beta[3]
se_beta_3 = np.sqrt(beta_var[3])
t_stat = beta_3 / se_beta_3
p_value = 1 - t.cdf(t_stat, n - p)

print(f"Статистика t: {t_stat}, p-значение: {p_value}")

if p_value < alpha:
    print("Отвергаем H0: Чем больше энергичность, тем больше популярность.")
else:
    print("Не отвергаем H0.")


# Модель H0: только свободный коэффициент и энергия
X_H0 = X[:, [0, 3]]
beta_H0 = np.linalg.inv(X_H0.T @ X_H0) @ X_H0.T @ y
e_H0 = y - X_H0 @ beta_H0
SS_res_H0 = e_H0.T @ e_H0

# Модель H1: полная модель
F_stat = ((SS_res_H0 - SS_res) / 2) / (SS_res / (n - p))
p_value = 1 - f.cdf(F_stat, 2, n - p)

print(f"Статистика F: {F_stat}, p-значение: {p_value}")

if p_value < alpha:
    print("Отвергаем H0: Популярность зависит одновременно от продолжительности и танцевальности.")
else:
    print("Не отвергаем H0.")


