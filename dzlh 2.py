#1.Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, сообщая об ошибке в случае деления на ноль.
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

if number2 == 0:
    print("Ошибка: Деление на ноль невозможно.")
else:
    result = number1 / number2
    print("Результат деления:", result)
#2.Рассчитать стоимость покупки с учетом скидки в 35%, которая предоставляется покупателю, если сумма покупки превышает 20 у.е. Сумму покупки ввести с клавиатуры, а результаты округлить до сотых (копейки, центы и т.д.). Вывести на экран итоговую стоимость и размер предоставленной скидки.
total = float(input('Сумма покупки:'))
if total > 20:
    sale_total = total * 0.65
    print('Сумма к оплате:', (round(sale_total, 2)))
else:
    print('Сумма к оплате:', (round(total, 2)))
#3 Напишите скрипт, который по введенному пользователем числу от 1 до 12, будет выводить на экран сообщение в виде названия месяца и времени года. Если пользователь введет недопустимое число, программа должна выдавать сообщение об ошибке.
month_number = int(input("Введите число от 1 до 12: "))

months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

seasons = ["Зима", "Весна", "Лето", "Осень"]

if 1 <= month_number <= 12:
    month = months[month_number - 1]
    season = seasons[(month_number % 12) // 3]
    print(f"Вы выбрали месяц {month} и это {season}.")
else:
    print("Ошибка: Введите число от 1 до 12.")