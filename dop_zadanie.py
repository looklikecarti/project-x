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


#(дополнительное задание номер 4)
#There's no such thing as private properties on a coffeescript object! But, maybe there are? Implement a function createSecretHolder(secret) which accepts any value as secret and returns an object with ONLY two methods getSecret() which returns the secret setSecret() which sets the secret obj = createSecretHolder(5) obj.getSecret() # returns 5 obj.setSecret(2) obj.getSecret() # returns 2
def createSecretHolder(secret):
    secret_value = secret
    def getSecret():
        return secret_value

    def setSecret(new_secret):
        nonlocal secret_value  # Используем nonlocal для изменения внешней переменной
        secret_value = new_secret
    return {
        'getSecret': getSecret,
        'setSecret': setSecret
    }
# Пример использования:
obj = createSecretHolder(5)
print(obj['getSecret']())
obj['setSecret'](2)
print(obj['getSecret']())


#(дополнительное задание номер 5)
def is_wristband(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    if rows == 0 or cols == 0:
        return False
    for i in range(rows):
        if matrix[i] != matrix[0]:
            return False
    for j in range(cols):
        if [matrix[i][j] for i in range(rows)] != matrix[0]:
            return False
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] != matrix[i - 1][j - 1]:
                return False
    for i in range(1, rows):
        for j in range(cols - 1):
            if matrix[i][j] != matrix[i - 1][j + 1]:
                return False
    return True
print(is_wristband([["A", "A"], ["B", "B"], ["C", "C"]]))
print(is_wristband([["A", "B"], ["A", "B"], ["A", "B"]]))
print(is_wristband([["A", "B", "C"], ["C", "A", "B"], ["B", "C", "A"], ["A", "B", "C"]]))
print(is_wristband([["A", "B", "C"], ["B", "C", "A"], ["C", "A", "B"], ["A", "B", "A"]]))


#(дополнительное задание № 6)
# Krazy King BlackJack is just like blackjack, with one difference: the kings! Instead of the kings being simply worth 10 points, kings are worth either 10 points or some other number of points announced by the dealer at the start of the game. Whichever value yields the best hand is the one that plays (much like how aces are worth either 1 or 11 points).
# Write a function that inputs a list of strings (representing a blackjack hand) and an integer that represents the alternative king value. The function should output an integer representing the value of the hand if it is less than or equal to 21, and False if it exceeds 21. Other than the alternative king value, normal blackjack rules apply.
# The cards, in order ace-through king, are represented as strings as follows:
# ['A', '2', '3','4', '5', '6','7', '8', '9','10', 'J', 'Q','K']
# A hand has between 2 and 20 cards, inclusive. The alternative king value is between 2 and 9, inclusive.
# Blackjack rules: the value of a hand is determined by maximizing the value of the sum of its cards while not exceeding 21 if possible. Number cards are worth their value, Jacks ('J') and Queens ('Q') are worth 10, Aces are worth either 1 or 11, and kings, again, are worth either 10 or their alternative value.
def krazy_king_blackjack(hand, king_value):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': king_value}
    total = 0
    num_aces = hand.count('A')
    for card in hand:
        total += card_values[card]
    while num_aces > 0 and total + 10 <= 21:
        total += 10
        num_aces -= 1
    if total > 21:
        return False
    return total
# Пример использования:
hand = ['A', 'K', '5', '4']
king_value = 9
result = krazy_king_blackjack(hand, king_value)
if result is False:
    print("Перебор!")
else:
    print("Значение руки:", result)
