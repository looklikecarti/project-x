'''#1 Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле article.txt со следующим содержимым:
def read_last(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        print("Количество строк должно быть положительным целым числом.")
        return
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines_list = f.readlines()
            lines_to_print = lines_list[-lines:]
            for line in lines_to_print:
                print(line.strip())
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
read_last(6, "article.txt")'''


#2 Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
import os
def print_docs(directory):
    for root, dirs, files in os.walk(directory):
        print(f"Папка: {root}")
        for file in files:
            print(f"Файл: {os.path.join(root, file)}")
print_docs("D:")
'''#3 Документ article.txt содержит следующий текст:
#Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
def longest_words(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            words = text.split()
            if not words:
                print("Файл не содержит слов.")
                return
            max_length = max(len(word) for word in words)
            longest_words_list = [word for word in words if len(word) == max_length]
            if len(longest_words_list) == 1:
                print(f"Самое длинное слово: {longest_words_list[0]}")
            else:
                print("Самые длинные слова:")
                for word in longest_words_list:
                    print(word)
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
longest_words("article.txt")
#4.Составьте программу - простейший редактор текстовых файлов. Алгоритм работы программы:
#Программа предлагает ввести имя будущего файла. Записывает его, присваивая расширение .txt.
#Программа предлагает записать строку в файл. При каждом нажатии кнопки ENTER происходит запись строки и переход на новую строчку.
#Если строка пустая или спец. символ - программа сохраняет файл.
#Требуется создать csv-файл rows_300.csv со следующими столбцами:
#– № - номер по порядку (от 1 до 300);
#– Секунда – текущая секунда на вашем ПК;
#– Микросекунда – текущая миллисекунда на часах.
#На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.
def text_editor():
    file_name = input("Введите имя будущего файла (без расширения): ") + ".txt"
    with open(file_name, 'w', encoding='utf-8') as file:
        while True:
            line = input("Введите строку (нажмите Enter для сохранения, либо введите '.' для выхода): ")
            if line == '.':
                break
            file.write(line + '\n')

    print(f"Файл '{file_name}' сохранен.")
text_editor()

import csv
import time
# Создаем CSV-файл
with open('rows_300.csv', 'w', newline='') as csvfile:
    fieldnames = ['№', 'Секунда', 'Миллисекунда']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1, 301):
        current_time = time.time()
        sec = int(current_time)
        msec = int((current_time - sec) * 1000)
        writer.writerow({'№': i, 'Секунда': sec, 'Миллисекунда': msec})
print("CSV-файл 'rows_300.csv' создан.")
# 5 При помощи библиотеки Pillow в директории circles (создайте ее во время выполнения функции) нарисуйте и сохраните 100 кругов радиусом 300 пикселей случайных цветов в формате jpg на белом фоне (каждый круг - отдельный файл). Для этого напишите функцию circles_generator(num_of_circles=100).
# from random import randint
# import os
# from PIL import Image, ImageDraw
from random import randint
import os
from PIL import Image, ImageDraw
def circles_generator(num_of_circles=100):
    # Создайте директорию 'circles', если она не существует
    if not os.path.exists('circles'):
        os.makedirs('circles')
    for i in range(num_of_circles):
        # Создаем новое изображение с белым фоном
        image = Image.new('RGB', (600, 600), color='white')
        # Создаем объект ImageDraw для рисования на изображении
        draw = ImageDraw.Draw(image)
        # Генерируем случайный цвет
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        # Генерируем случайные координаты для центра круга
        x = randint(0, 600)
        y = randint(0, 600)
        # Рисуем круг радиусом 300 пикселей с выбранным цветом
        draw.ellipse((x - 300, y - 300, x + 300, y + 300), fill=color)
        # Сохраняем изображение как файл с именем, содержащим номер
        image.save(f'circles/circle_{i+1}.jpg')
        print(f"Создан файл 'circle_{i+1}.jpg'")
circles_generator()'''