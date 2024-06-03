import numpy as np
import pandas as pd
from scipy.stats import norm, chi2
from scipy.stats import kstest, mannwhitneyu, kruskal


# Загрузка данных
data = pd.read_csv('sex_bmi_smokers (1).csv')
bmi = data['bmi']

#Критерий Пирсона хи-квадрат
#Основная гипотеза (H0): Индекс массы тела (ИМТ) распределен нормально.
#Альтернативная гипотеза (H1): Индекс массы тела (ИМТ) не распределен нормально.

print('=====================  Задание 1  =====================\n')
print("Критерий Пирсона хи-квадрат: \n")

# Параметры нормального распределения
mean_bmi = np.mean(bmi)
std_bmi = np.std(bmi)

# Разбиение на интервалы (например, квантильное разбиение на 10 интервалов)
quantiles = np.percentile(bmi, np.linspace(0, 100, 11))
observed_freq = np.histogram(bmi, bins=quantiles)[0]

# Теоретические частоты
expected_freq = len(bmi) * (norm.cdf(quantiles[1:], mean_bmi, std_bmi) - norm.cdf(quantiles[:-1], mean_bmi, std_bmi))

# Статистика хи-квадрат
chi2_stat = ((observed_freq - expected_freq) ** 2 / expected_freq).sum()

# Степени свободы
df = len(observed_freq) - 1 - 2  # число интервалов - 1 - число оцениваемых параметров (среднее и стандартное отклонение)

# Критическое значение
chi2_critical = chi2.ppf(0.95, df)

# Проверка гипотезы
if chi2_stat < chi2_critical:
    print("Не отвергаем H0: ИМТ распределен нормально.\n")
else:
    print("Отвергаем H0: ИМТ не распределен нормально.\n")


#Альтернативный критерий (Критерий Колмогорова-Смирнова)
#Основная гипотеза (H0): Индекс массы тела (ИМТ) распределен нормально.
#Альтернативная гипотеза (H1): Индекс массы тела (ИМТ) не распределен нормально.


print("Альтернативный критерий (Критерий Колмогорова-Смирнова): \n")

# Нормализация данных
normalized_bmi = (bmi - mean_bmi) / std_bmi

# Тест Колмогорова-Смирнова
kstest_result = kstest(normalized_bmi, 'norm')

print(f"Статистика KS: {kstest_result.statistic}, p-значение: {kstest_result.pvalue}")

if kstest_result.pvalue > 0.05:
    print("Не отвергаем H0: ИМТ распределен нормально.\n")
else:
    print("Отвергаем H0: ИМТ не распределен нормально.\n")


#Задание 2: Проверка однородности индекса массы тела курящих и некурящих
#Гипотезы
#Основная гипотеза (H0): Распределение ИМТ одинаково для курящих и некурящих.
#Альтернативная гипотеза (H1): Распределение ИМТ различается для курящих и некурящих.

print('=====================  Задание 2  =====================\n')
print('Критерий хи-квадрат\n')

# Разделение данных
smokers = data[data['smoker'] == 'yes']['bmi']
non_smokers = data[data['smoker'] == 'no']['bmi']

# Квантильное разбиение на интервалы
bins = np.percentile(data['bmi'], np.linspace(0, 100, 11))

observed_smokers = np.histogram(smokers, bins=bins)[0]
observed_non_smokers = np.histogram(non_smokers, bins=bins)[0]

# Ожидаемые частоты
total = len(smokers) + len(non_smokers)
expected_smokers = len(smokers) / total * (observed_smokers + observed_non_smokers)
expected_non_smokers = len(non_smokers) / total * (observed_smokers + observed_non_smokers)

# Статистика хи-квадрат
chi2_stat = ((observed_smokers - expected_smokers) ** 2 / expected_smokers).sum() + \
            ((observed_non_smokers - expected_non_smokers) ** 2 / expected_non_smokers).sum()

# Степени свободы
df = len(bins) - 1 - 1

# Критическое значение
chi2_critical = chi2.ppf(0.95, df)

# Проверка гипотезы
if chi2_stat < chi2_critical:
    print("Не отвергаем H0: Распределение ИМТ одинаково для курящих и некурящих.\n")
else:
    print("Отвергаем H0: Распределение ИМТ различается для курящих и некурящих.\n")


#Альтернативный критерий (Критерий Манна-Уитни)
print('Альтернативный критерий (Критерий Манна-Уитни):\n')

# Тест Манна-Уитни
u_stat, p_value = mannwhitneyu(smokers, non_smokers)

print(f"Статистика U: {u_stat}, p-значение: {p_value}")

if p_value > 0.05:
    print("Не отвергаем H0: Распределение ИМТ одинаково для курящих и некурящих.\n")
else:
    print("Отвергаем H0: Распределение ИМТ различается для курящих и некурящих.\n")


# Задание 3: Проверка независимости индекса массы тела и пола
# Гипотезы
# Основная гипотеза (H0): Индекс массы тела независим от пола.
# Альтернативная гипотеза (H1): Индекс массы тела зависит от пола.

print('=====================  Задание 3  =====================\n')

#Критерий хи-квадрат

print('Критерий хи-квадрат:\n')
# Разделение данных на группы
males = data[data['sex'] == 'male']['bmi']
females = data[data['sex'] == 'female']['bmi']

# Квантильное разбиение на интервалы
bins = np.percentile(data['bmi'], np.linspace(0, 100, 11))

observed_males = np.histogram(males, bins=bins)[0]
observed_females = np.histogram(females, bins=bins)[0]

# Создание таблицы сопряженности
observed = np.array([observed_males, observed_females])

# Ожидаемые частоты
total = observed.sum()
row_sums = observed.sum(axis=1).reshape(-1, 1)
col_sums = observed.sum(axis=0).reshape(1, -1)
expected = row_sums @ col_sums / total

# Статистика хи-квадрат
chi2_stat = ((observed - expected) ** 2 / expected).sum()

# Степени свободы
df = (observed.shape[0] - 1) * (observed.shape[1] - 1)

# Критическое значение
chi2_critical = chi2.ppf(0.95, df)

# Проверка гипотезы
if chi2_stat < chi2_critical:
    print("Не отвергаем H0: Индекс массы тела независим от пола.\n")
else:
    print("Отвергаем H0: Индекс массы тела зависит от пола.\n")


#Альтернативный критерий (Тест Краскела-Уоллиса)
print('Альтернативный критерий (Тест Краскела-Уоллиса):\n')

kruskal_stat, p_value = kruskal(males, females)

print(f"Статистика Краскела-Уоллиса: {kruskal_stat}, p-значение: {p_value}")

if p_value > 0.05:
    print("Отвергаем H0: Распределение ИМТ одинаково для мужчин и женщин.")
else:
    print("Не отвергаем H0: Распределение ИМТ различается для мужчин и женщин.")
