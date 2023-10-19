#(дополнительное задание номер 1)
# Написать программу, которая будет делить введенные пользователем два вещественных числа и выводить результат на экран, сообщая об ошибке в случае деления на ноль.
number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))

if number2 == 0:
    print("Ошибка: Деление на ноль невозможно.")
else:
    result = number1 / number2
    print("Результат деления:", result)


#(дополнительное задание номер 2)
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)
# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)
# Note: The function accepts an integer and returns an integer.
# Happy Coding!
Znach = str(input('Введите число:'))
NewZnach = ''
for i in Znach:
    NewZnach += str(int(i) ** 2)
print(NewZnach)

#(дополнительное задание номер 3)
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
# Notes
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!
def word_converter(word):
    word = word.lower()
    result = ''
    for el in word:
        if word.count(el) > 1:
            result += ')'
        else:
            result += '('
    return result
print(word_converter(str(input('Введите строку:'))))


#!!!!!!!!!!!!!!!!!!!посмотрите мой гитхаб и поставьте баллы, пожалуйста!!!!!!!!!!!!!!!!!!!!!!!!!
# https://github.com/looklikecarti