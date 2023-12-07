import os
import re
import numpy as np
import pandas as pd
from google.colab import drive
import matplotlib.pyplot as plt

# Подключение Google Drive
drive.mount('/content/drive')

# Загрузка данных
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/files/ff_3333.dat', delimiter=' ', header=None)
df.rename(columns={0: 'Frequency', 1: 'Amplitude'}, inplace=True)


# 1. Средняя доходность женщин
# Предположим, что в данных есть столбец "пол" и "доход"
# Фильтрация данных по женщинам
female_data = df[df['Gender'] == 'female']
average_income_female = female_data['Income'].mean()
print(f'Средняя доходность женщин: {average_income_female}')


# 2. Люди с бОльшими расходами
# Предположим, что в данных есть столбец "расходы"
# Группировка по полу и поиск максимальных расходов
max_expenses_by_gender = df.groupby('Gender')['Expenses'].max()
print('Максимальные расходы по полу:\n', max_expenses_by_gender)


# 3. График зависимости доходов от возраста для мужчин
# Предположим, что есть столбец "возраст"
# Фильтрация данных по мужчинам
male_data = df[df['Gender'] == 'male']
plt.scatter(male_data['Age'], male_data['Income'])
plt.title('График зависимости доходов от возраста для мужчин')
plt.xlabel('Возраст')
plt.ylabel('Доход')
plt.show()


# 4. Столбчатый график для распределения расходов от доходов для мужчин и женщин
# Предположим, что есть столбец "расходы"
# Создание нового столбца "GenderColor" для цветового отличия мужчин и женщин
df['GenderColor'] = df['Gender'].map({'male': 'blue', 'female': 'pink'})
plt.bar(df['Income'], df['Expenses'], color=df['GenderColor'])
plt.title('Распределение расходов от доходов')
plt.xlabel('Доход')
plt.ylabel('Расходы')
plt.show()