#1 Создать объект pandas Series из листа, объекта NumPy, и словаря
import pandas as pd
import numpy as np
my_list = [1, 2, 3, 4, 5]
my_array = np.array([10, 20, 30, 40, 50])
my_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
series_from_list = pd.Series(my_list)
series_from_array = pd.Series(my_array)
series_from_dict = pd.Series(my_dict)
print("Series из списка:")
print(series_from_list)
print("\nSeries из массива NumPy:")
print(series_from_array)
print("\nSeries из словаря:")
print(series_from_dict)


#2 Получить не пересекающиеся элементы в двух объектах Series
import pandas as pd
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([4, 5, 6, 7, 8])
not_common_in_series1 = series1[~series1.isin(series2)]
not_common_in_series2 = series2[~series2.isin(series1)]
print("Элементы, которые есть только в первой Series:")
print(not_common_in_series1)
print("\nЭлементы, которые есть только во второй Series:")
print(not_common_in_series2)


#3 Узнать частоту уникальных элементов объекта Series (гистограмма)
import pandas as pd
import matplotlib.pyplot as plt
series = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5])
value_counts = series.value_counts()
value_counts.plot(kind='bar')
plt.title('Гистограмма уникальных элементов')
plt.xlabel('Уникальные элементы')
plt.ylabel('Частота')
plt.show()


#4 Объединить два объекта Series вертикально и горизонтально
import pandas as pd
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
vertical_concatenation = pd.concat([series1, series2])
print("Вертикальное объединение:")
print(vertical_concatenation)
import pandas as pd
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
horizontal_concatenation = pd.concat([series1, series2], axis=1)
print("Горизонтальное объединение:")
print(horizontal_concatenation)


#5 Найти разность между объектом Series и смещением объекта Series на n
import pandas as pd
my_series = pd.Series([1, 3, 5, 7, 9])
n = 2
difference = my_series - my_series.shift(n)
print("Исходная Series:")
print(my_series)
print("\nРазность между Series и его смещением на", n, "позиции:")
print(difference)