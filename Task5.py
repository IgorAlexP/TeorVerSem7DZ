"""Заявляется, что партия изготавливается со средним арифметическим 2,5 см. 
Проверить данную гипотезу, если известно, что размеры изделий подчинены нормальному закону распределения. 
Объем выборки 10, уровень статистической значимости 5%
2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34"""

from scipy.stats import t
import math

def ttest_1samp(sample, population_mean):
    n = len(sample)  # размер выборки
    sample_mean = sum(sample) / n  # среднее значение выборки
    sample_variance = sum([(x - sample_mean)**2 for x in sample]) / (n - 1)  # выборочная дисперсия
    standard_error = math.sqrt(sample_variance / n)  # стандартная ошибка среднего

    t_statistic = (sample_mean - population_mean) / standard_error  # статистика t
    degrees_of_freedom = n - 1  # степени свободы

    # Расчет p-значения с использованием функции распределения t-статистики (двусторонний тест)
    p_value = 2 * (1 - t.cdf(abs(t_statistic), degrees_of_freedom))

    return t_statistic, p_value

sample = [2.51, 2.35, 2.74, 2.56, 2.40, 2.36, 2.65, 2.7, 2.67, 2.34]
population_mean = 2.5
alpha = 0.05

statistic, p_value = ttest_1samp(sample, population_mean)

print("Статистика t:", statistic)
print("p-значение:", p_value)

if p_value < alpha:
    print("Отвергаем нулевую гипотезу. Среднее значение не равно 2.5 см.")
else:
    print("Не отвергаем нулевую гипотезу. Среднее значение равно 2.5 см.")


"""
Статистика t: 0.5630613661802959
p-значение: 0.5871439993940628
Не отвергаем нулевую гипотезу. Среднее значение равно 2.5 см."""