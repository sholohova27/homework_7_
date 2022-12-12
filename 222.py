# def greeting()-> str:
#     # print(f"Hello {name}")
#       return f"Hello"
# # #
#
# print(greeting())

# print(greeting("Alisa"))

# ARGS(*) & KWARGS(**)

# def nar(**name):
#     for key, value in name.items():
#         print(key,value)
#
# nar(first_name = "1")

# def invite_to_event(username):
#     print(f"Dear {username},\nwe have the honour to invite you to our event.")
# invite_to_event("Nataly")

# def add_ten(a):
#     b = 10
#     return a + b
#
#
# print(add_ten(6))  # 16

# a = 5
# b = 0
#
#
# def fun():
#     global a
#     a = 10
#     b = 2
#
# fun()
# print(a)  # 10
# print(b)  # 0


# base_rate = 40
# price_per_km = 10
# total_trip = 0
#
#
# def trip_price(path: float):
#     price_per_trip = base_rate + price_per_km * path
#     print(price_per_trip)
#
#     def counter(): #считает сколько раз вызвана ф-я
#         global total_trip
#         total_trip += 1
#         print(total_trip)
#
#     counter()




# base_rate = 40
# price_per_km = 10
# total_trip = 0
#
#
# def trip_price(path: float):
#     global total_trip #считает сколько раз вызвана ф-я
#     total_trip += 1
#     price_per_trip = base_rate + price_per_km * path
#     return price_per_trip


# def func_outer():
#     x = 2
#
#     def func_inner():
#         nonlocal x
#         x = 5
#
#     func_inner()
#     return x
#
#
# result = func_outer()  # 5
# print(result)
#
# def discount_price(price:float, discount:float)->float:
#     def apply_discount():
#         # nonlocal price
#         # nonlocal discount
#         if 0 < discount < 1:
#             price_with_discount = price * (1-discount)
#         else:
#             price_with_discount = price
#         return price_with_discount
#
#     return apply_discount()
# print(discount_price(100.0, 0.2))


# def fun(a, b=2, c=3):
#     return a + b * c
#
# print(fun(2))

# def get_fullname(first_name:str, last_name, middle_name = False):
#     if middle_name is False:
#         return f"{first_name} {last_name}"
#     else:
#         return f"{first_name} {middle_name} {last_name}"
#
#
# print(get_fullname('Nataly','Sholohova','Leonidovna'))
#
# def fun(a, b=2, c=3):
#     return a + b * c
# #
#
# print(fun(b=4, c=4, a=2))  # 18
# print(fun(c=1, a=2, b=3))  # 5
# print(fun(c=3, b=2, a=7))  # 13

# def format_string(string, length):
#     if len(string) >= length:
#         string
#     else:
#         string = " " * ((length - len(string)) // 2) + string
#     return string
#
# print(format_string("Nataly",7))

# # # # #
# def first(size, *args):
#     n = size + len(args)
#     return float(n)
#
# def second(size, **kwargs):
#     n = size + len(kwargs)
#     return float(n)
#
# print(second(3, comment_one="first", comment_two="second", comment_third="third"))

# def modeling(factor, *_, correction):
#     result = 0
#     # for number in numbers:
#     #     result += number * factor
#     # result = result - correction
#     return result
#
#
# print(modeling(10,2,3, correction = 2))  # 58


# def cost_delivery(quantity, *args, discount=0):
#     if 0 < discount < 1:
#         price_with_discount = (5 + 2 * (quantity - 1)) * (1-discount)
#     else:
#         price_with_discount = 5 + 2 * (quantity - 1)
#     return price_with_discount
#
#
# print(cost_delivery(2))
""" Factorial теория"""
# Вычисляем факториал числа n с помощью рекурсии
# @param n – число, для которого надо рассчитать факториал
# @return – факториал числа n
# def factorial(n):
#     if n < 2:
#         return 1  # Базовый случай
#     else:
#         return n * factorial(n - 1)  # Рекурсивный случай
#
#
# num = int(input("Введите положительное целое число: "))
# result = factorial(num)
# print(f"Факториал числа {num} равен {result}")

""" Factorial практика"""
# def factorial(n):
#     if n < 2:
#         return 1  # Базовый случай
#
#     else:
#         return n * factorial(n - 1)  # Рекурсивный случай
# print(factorial(50))

# def number_of_groups(n, k):
#     if n < 2:
#         return 1
#     else:
#         return int(factorial(n)/(factorial(n - k)*factorial(k)))
# #
# print(number_of_groups(50,7))

################херня какая-то
# def fibonacci(n:int):
#     for number in range(n+1):
#         if number <= 1:
#             print(number)
#         else:
#             print(fibonacci(number-1) + fibonacci(number-2))
################
#
# fibonacci(5)

# sum_ = 0
# for number in range(1,3):
#     # print(number)
#     sum_ += number
# print(sum_)

""" Fibonacci """
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(5))

# number = 5
#
# for n in range(number):
#     print(fibonacci(n))
###### или 1 раз указываем во вложенной ф-ции
# def fibonacci_sequence():
#     number = fibonacci(6)
#
#     for n in range(number):
#         print(fibonacci(n))
# #
# #
# fibonacci_sequence()



# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'равно', b)
#     else:
#         print(b, 'максимально')
#
# print_max(3, 4)  # прямая передача значений
#
# x = 5
# y = 7
# print_max(x, y)  # передача переменных в качестве аргументов

# x = 50
#
# def func():
#     global x
#     x = 2
#     print('Замена локального x на', x)  # Замена локального x на 2
#
# func()
# print('x по-прежнему', x)   # x по-прежнему 50

# def func(a, b=5, c=10):
#     print('a равно', a,', b равно', b,', а c равно', c)
#
# # func(3, 7)          # a равно 3, b равно 7, а c равно 10
# # func(25, c=24)      # a равно 25, b равно 5, а c равно 24
# # func(c=50, a=100)   # a равно 100, b равно 5, а c равно 50


# def say(message, times=1):
#     print(message * times)
#
# say('Привет')   # Привет
# say('Мир', 5)   # МирМирМирМирМир

# def total(a=5, *numbers, **phone_book):
#     print('a', a)
#     # проход по всем элементам кортежа
#     for single_item in numbers:
#         print('single_item', single_item)
#
#     #проход по всем элементам словаря
#     for first_part, second_part in phone_book.items():
#         print(first_part,second_part)
#
# print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))
#
# not_empty = {"key": "value"}
# not_empty["new_key"] = "new value"
# print(not_empty)    # {"key": "value", "new_key": "new value"}

# import math
#
# sin_pi = math.sin(math.pi)
# print(sin_pi)

# from math import pi, sin
#
# sin_pi = sin(pi)
# print(sin_pi)

    # def say_hello(name):
    #     print(f'Hello {name}')
    #
    # def main():
    #     print("You imported hello.py")
    #     say_hello('user')
    #
    # if __name__ == '__main__':
    #     main()
# Рекурсия - аналог цикла с условием
# def fun(n):
#     if n==3:
#         return 3 #возвращает только от числа в условии
#     return fun(n-1) + n
#
#
# result = fun(6)
# print(result)#12

#
# chars = ['a', 'b', 'c', 'a']
# a_count = chars.count('a')
# print(a_count) # 2


# numbers = {1, 2, 3}
# numbers.discard(5)
# print(numbers)    # {1, 2}


# from pathlib import Path

# p = Path('C:/Users/Ioan/Desktop')    # p Указывает на папку
# for i in p.iterdir():
#     print(i.name)   # Выведет в цикле имена всех папок и файлов в папке

# import sys
#
# def main():
#     for arg in sys.argv:
#         print(arg)
# main()

# list_ = [1, 1, 5]
# for element in list_:
#     print(element)


# def game(terra, power):
#     for element in terra:
#         for index in element:
#             if index > power:
#                 break
#             if index <= power:
#                 power += index
#     return power
#
#
# print(game([[1, 1, 5, 10], [10, 2], [1, 1, 1]], 1))

"""Task 4.10"""

# from random import randint
#
# def get_random_password():
#     password = ""
#     count = 0
#     while count < 8:
#         random_num = chr(randint(40, 126))
#         password = password + random_num
#         count = count + 1
#     return password


"""Task 4.11"""
#Вариант 1
# def is_valid_password(password):
#     count_int = 0
#     count_up = 0
#     count_low = 0
#     if len(password) == 8:
#         for symbol in password:
#             if symbol in '01234567890':
#                 count_int += 1
#             if symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#                 count_up += 1
#             if symbol in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
#                 count_low += 1
#         if count_int >= 1 and count_up >= 1 and count_low >= 1:
#             return True
#         else:
#             return False
#     else:
#         return False
#Вариант 2
# def is_valid_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#     if len(password) == 8 and has_upper and has_lower and has_num:
#         return True
#     return False
# # print(is_valid_password(get_random_password()))
#
#
"""Task 4.12"""
#
# def get_password():
#     count = 0
#     while count < 100:
#         password = get_random_password()
#         count += 1
#         if is_valid_password(password):
#             return password
#             break
#
#
# print(get_password())

"""Task 4.13"""
from pathlib import Path


# def parse_folder(path):
#     files = []
#     folders = []
#     p = Path(path)
#     for i in p.iterdir():
#         if i.is_dir():
#             folders.append(i.name)
#         if i.is_file():
#             files.append(i.name)
#     tup = (files, folders)
#     return tup

# print(parse_folder('C:\\Users\Ioan\Desktop\Отчеты\Reprocessing'))

"""Task 4.14"""
# import sys
#
# Вариант 1
# def parse_args():
#     result = ""
#     for arg in sys.argv[1:]:
#         result += arg
#         result += " "
#     return result[:-1]

# Вариант 2
# def parse_args():
#     result = " ".join(sys.argv[1:])
#     return result


# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
#
# print(x)

# one_line_text = "Textual data in Python is handled with str objects, or strings. "\
#                 "Strings are immutable sequences of Unicode code points. "\
#                 "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
#
# jingle_bells = "Jingle bells, jingle bells\tJingle all the way\tOh, what fun it is to ride\tIn a one horse open sleigh"
# print(jingle_bells)

# map = {ord('з'): 'z', ord('ю'): 'u', ord('t'): 'y'}
# translated = 'зюt'.translate(map)
# print(translated) # zu
#
# # a = ord('ю')
# # print(a)


# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)



# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))


# s =  "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
# print(s)  # 'Bob' Dilan

# print('pi: {:0.3}'.format(3.1415))  # pi: 3.14


# print('"{}" "{:+}" "{:-}" "{: }"'.format(1, 2, -3, 4))  # "1" "+2" "-3" " 4"

# print("|{:<10}|{:*^10}|{:>10}|".format('left', 'center', 'right'))  # |left      |**center**|     right|

"""Task 5.1"""


# def real_len(text):
#     list = []
#     for sym in text:
#         if sym not in ('\n', '\f', '\r', '\t', '\v'):
#             list.append(sym)
#     lengts = int(len(list))
#     return lengts
#
#
# print(real_len('Al\nKdfe23\t\v.\r'))


# message = "Hello my little friend!"
#
# print(message.find("li", 5, 15))  # 9
# print(message.find("l", 0, 2))  # -1
# print(message.find("li"))  # 9

"""Task 5.2"""
#
# articles_dict = [
#     {
#         "title": "Endless ocean waters.",
#         "author": "Jhon Stark",
#         "year": 2019,
#     },
#     {
#         "title": "Oceans of other planets are full of silver",
#         "author": "Artur Clark",
#         "year": 2020,
#     },
#     {
#         "title": "An ocean that cannot be crossed.",
#         "author": "Silver Name",
#         "year": 2021,
#     },
#     {
#         "title": "The ocean that you love.",
#         "author": "Golden Gun",
#         "year": 2021,
#     },
# ]

# def find_articles(key, letter_case=False):
#     l = []
#     for element in articles_dict:
#         if not letter_case:
#             if key.lower() in element['title'].lower() or key.lower() in element['author'].lower():
#                 l.append(element)
#         if letter_case:
#             if key in element['title'] or key in element['author']:
#                 l.append(element)
#     return l
#
# print(find_articles('that', letter_case = False))

# l = "Oceans of other planets are full of silver"
# if "Ocean".lower() in l.lower():
#     print("True")


# chars = {'a': 1, 'b': "ff"}
# # c_idx = chars.get('b', -1)
# c_idx = chars['b']
# print(type(c_idx))  # -1

"""Task 5.3"""
# def sanitize_phone_number(phone):
#     num = phone.replace("+", " ").replace("-", " ").replace(")", " ").replace("(", " ").strip().split(" ")
#     num = "".join(num)
#     return (num)
#
#
# print(sanitize_phone_number("38050 111 22 11   "))

"""Task 5.4"""

# def is_check_name(fullname, first_name):
#     if fullname.find(first_name) != -1:
#         return True
#     else:
#         return False

"""Task 5.5"""
# Вариант 1 (мой)
# def sanitize_phone_number(phone):
#     num = phone.replace("+", " ").replace("-", " ").replace(")", " ").replace("(", " ").strip().split(" ")
#     num = "".join(num)
#     return (num)
# #
# def get_phone_numbers_for_countries(list_phones):
#     country_phones = {"JP": [], "SG": [], "TW": [], "UA": []}
#     for phone in list_phones:
#         clear_phone = sanitize_phone_number(phone)
#         if clear_phone.find('81', 0, 2) == 0:
#             country_phones["JP"].append(clear_phone)
#         elif clear_phone.find('65', 0, 2) == 0:
#             country_phones["SG"].append(clear_phone)
#         elif clear_phone.find('886', 0, 3) == 0:
#             country_phones["TW"].append(clear_phone)
#         else:
#             country_phones["UA"].append(clear_phone)
#     return country_phones
#

# Вариант 2 (ф-ция removeprefix с версии py 3.9, а у меня 3.7 - будет ругаться
# def sanitize_phone_number(phone):
#     new_phone = (
#         phone.strip()
#         .removeprefix("+")
#         .replace("(", "")
#         .replace(")", "")
#         .replace("-", "")
#         .replace(" ", "")
#     )
#     return new_phone
# def get_phone_numbers_for_countries(list_phones):
#     country_phones = {"JP": [], "SG": [], "TW": [], "UA": []}
#      for phone in list_phones:
#         clear_phone = sanitize_phone_number(phone)
#         if clear_phone[0:2] == '81:
#             country_phones["JP"].append(clear_phone)
#         elif clear_phone[0:2] == '65':
#             country_phones["SG"].append(clear_phone)
#         elif clear_phone[0:3] == '886':
#             country_phones["TW"].append(clear_phone)
#         else:
#             country_phones["UA"].append(clear_phone)
#     return country_phones
#
# print(get_phone_numbers_for_countries(["81050 311 22 11   ", "+38050511-22 12 ", "88650 311 22 11   "]))

"""Task 5.6"""
# def is_spam_words(text, spam_words, space_around=False):
#     space = False
#     for spam_word in spam_words:
#         if not space_around:
#             if spam_word.lower() in text.lower():
#                 return True
#             else:
#                 return False
#         if space_around:
#             for txt in text.replace(".", " ").replace(",", " ").replace("!", " ").strip().split(" "):
#                 if spam_word.lower().strip() == txt.lower():
#                     space = True
#             return space
#
# print(is_spam_words("Ты хорош но выглядишь как лох. ", ["лох"], True))

"""Task 5.7"""
# CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
#
# TRANS = {}
#
# for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
#     TRANS[ord(c.upper())] = t.upper()
#     TRANS[ord(c)] = t
#
#
# def translate(name):
#     return name.translate(TRANS)
#
# print(translate("Ната"))



"""Task 5.8"""
# grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
# students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}


# def formatted_grades(students):
#     counter = 0
#     col_1 = []
#     col_2 = []
#     col_3 = []
#     col_4 = []
#     final_list = []
#     for key, value in students.items():
#         counter += 1
#         col_1.append(counter)
#         col_2.append(key)
#         col_3.append(value)
#     # print(col_1)
#     # print(col_2)
#     # print(col_3)
#     for el in range(len(col_3)):
#         col_4.append(grades[col_3[el]])
#     # print(col_4)
#
#     for l_1, l_2, l_3, l_4 in zip(col_1, col_2, col_3, col_4):
#         final_list.append("{:>4}|{:<10}|{:^5}|{:^5}".format(l_1, l_2, l_3, l_4))
#     return(final_list)
#
#
# for i in formatted_grades(students):
#     print(i)

"""Task 5.9"""


# def formatted_numbers():
#     l = ["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
#     for i in range(16):
#         l.append("|{:<10d}|{:^10x}|{:>10b}|".format(i, i, i))
#     return l
#
#
# for el in formatted_numbers():
#     print(el)
"""Task 5.10"""
import re


# def find_word(text, word):
#     find_res = {'result': False,
#                 'first_index': None,
#                 'last_index': None,
#                 'search_string': word,
#                 'string': text
#                 }
#     if re.search(word, text):
#         first_index = re.search(word, text).span()[0]
#         last_index = re.search(word, text).span()[1]
#         if first_index >= 0:
#             find_res['result'] = True
#             find_res['first_index'] = first_index
#             find_res['last_index'] = last_index
#
#     return find_res
#
# print(find_word('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.',
#                 'python'))

"""Task 5.11"""

# def find_all_words(text, word):
#     find_ = re.findall(word, text, flags=re.IGNORECASE)
#     return find_

"""Task 5.12"""


# def replace_spam_words(text, spam_words):
#     for spam in spam_words:
#         if spam in text:
#             text = re.sub(spam, '*'*len(spam), text, flags=re.IGNORECASE)
#     return text
#
#
# print(replace_spam_words('Guido van Rossum began working onPython in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn',
#                     ['Python']))


"""Task 5.13"""
# def find_all_emails(text):
#     result = re.findall(r"[a-zA-Z]+[a-zA-Z0-9._]+@\w+\.\w{2,}\b", text)
#     return result
#
# print(find_all_emails('222111@test.com'))

"""Task 5.14"""
# def find_all_phones(text):
#
#     result = re.findall(r"([+]{1}[380]{3}[\(]{1}\d{2}[\)]{1}\d{3}[\-]{1}\d{1}[\-]{1}\d{3}|[+]{1}[380]{3}[\(]{1}\d{2}[\)]{1}\d{3}[\-]{1}\d{2}[\-]{1}\d{2})", text)
#     return result
#
# print(find_all_phones('Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'))

"""Task 5.15"""
# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"([h]{1}[t]{2}[p]{1}[s]?[\:]{1}[\/]{2}[w]{3}\.\w+\.\w{2,}\b|[h]{1}[t]{2}[p]{1}[s]?[\:]{1}[\/]{2}\w+\.\w{2,}\b)", text)
#     for match in iterator:
#         result.append(match.group())
#     return result
#
# print(find_all_links('The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com '))

#Варианты итераций re.finditer
# def find_all_links(text):
#     result = []
#     iterator = re.finditer(r"([h]{1}[t]{2}[p]{1}[s]?[\:]{1}[\/]{2}[w]{3}\.\w+\.\w{2,}\b|[h]{1}[t]{2}[p]{1}[s]?[\:]{1}[\/]{2}\w+\.\w{2,}\b)", text)
#     for match in iterator:
#         result.append(match.group())
#         result.append(match.start())
#         result.append(match.end())
#     return result



# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(2)#месторасположение курсора
#
# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'
#
# fh.close()

# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)
# print(byte_numbers)

# byte_str = 'some text'.encode()
# print(byte_str)

# for num in [127, 255, 156]:
#   print(hex(num))

"""Task 6.1"""
# def total_salary(path):
#     descriptor = open(path, 'r')
#     total = 0
#     while True:
#         line = descriptor.readline()# вытянули каждую строку
#         if not line:
#             break
#         salaries = float(line.split(",")[1])# превратили каждую строку в список, из каждого списка взяли только 2-й элемент с суммой - это снова строка
#         total += salaries
#     descriptor.close()
#     return total

#
# #
# print(total_salary('text.txt'))

"""Task 6.2"""
# def write_employees_to_file(employee_list, path):
#     descriptor = open(path, 'w')
#     text = ""
#     for element in employee_list:
#         for el in element:
#             text += str(el) + "\n"
#     descriptor.write(text)
#     descriptor.close()
#     return text
#
#
# print(write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],'C:/Users/Ioan/Desktop/test.txt'))

"""Task 6.3"""
# def read_employees_from_file(path):
#     descriptor = open(path, 'r')
#     l = [line.strip() for line in descriptor.readlines()]
#     descriptor.close()
#     return l
#
#
# print(read_employees_from_file('C:/Users/Ioan/Desktop/test.txt'))
"""Task 6.4"""
# def add_employee_to_file(record, path):
#     descriptor = open(path, 'a')
#     rec = descriptor.write(record+"\n")
#     descriptor.close()
#     return rec
#
# print(add_employee_to_file('Nataly Sholohova,23','C:/Users/Ioan/Desktop/test.txt'))

"""Task 6.5"""
# def get_cats_info(path):
#     with open(path, 'r') as reader:
#         reader = [line.strip() for line in reader]
#         records = []
#         for line in reader:
#             # print(line, end = '')
#             list_ = line.split(',')
#             records.append({"id": list_[0], "name": list_[1], "age": list_[2]})
#     return records
#
# print(get_cats_info('C:/Users/Ioan/Desktop/test.txt'))

# a = "a,1,c,2"
# b = a.split(",")
# print(b)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# odd_numbers = numbers[::2]
# print(odd_numbers)


# .CSV', '.PY', '.INI', '.SQL', '.JPEG', '.TWBX', '.XLS', '.PNG', '.JPG', '.TWB', '.PDF', '.MP4', '.XLSB', '.EML', '.DOCX', '.XLSX', '.LOG', '.EXE'
"""Buffering"""
# import io
# print("Default buffer size: ", io.DEFAULT_BUFFER_SIZE)
# with open('C:/Users/Ioan/Desktop/test.txt', mode = "r", buffering=5) as file:
#     print(file.line_buffering)
#     content = file.buffer
#     for line in content:
#         print(line.split())

"""Encoding"""
# with open('C:/Users/Ioan/Desktop/test.txt') as file:
#     print("Default encoding", file.encoding)
#
# with open('C:/Users/Ioan/Desktop/test.txt', encoding="utf-8") as file:
#     print("New encoding", file.encoding)
#
# import os
# os.makedir()


# p = Path('22-04-30-22-05-31-DisputeReport-AsgerLtd.Csv')
# print(p.suffix.upper().lstrip("."))


# import shutil
# filename = r"C:/Users/Ioan/Downloads/Archives/Downloads.rar"
# shutil.unpack_archive(filename)

# print("Hello")


# from dateutil import tz, parser
# from datetime import datetime, timedelta, date

# now = datetime.now(tz=tz.tzlocal())
# print(now)
# print("Timezone:", now.tzname())
#
# London_tz = tz.gettz("Europe/London")
# now1 = datetime.now(tz=London_tz)
# print(now1)
#
# new_date = parser.parse("December 07, 2022 8:25 PM")
# new_date = new_date.replace(tzinfo=tz.gettz("America/New_York"))
# now = datetime.now(tz.tzlocal())
# result = new_date - now
# print(result)
#
# from calendar import monthrange
# m = monthrange(2022, 12)
# print(m)

# now = datetime.now()
# # tomorrow = timedelta(days=+1)
# # print(now + tomorrow)
#
# from dateutil.relativedelta import relativedelta
#
# delta = relativedelta(years=+3, month=+1, days=+4, hours=+4, minutes=-25)
# print(now + delta)


# from datetime import date, datetime
#
# date.fromisoformat("2022-12-07")
# print(datetime.date)

"""Task 7.1"""
# from setuptools import setup
#
#
# def do_setup(args_dict):
#     setup(
#     name="useful",
#     version="1",
#     description="Very useful code",
#     url="http://github.com/dummy_user/useful",
#     author="Flying Circus",
#     author_email="flyingcircus@example.com",
#     license="MIT",
#     packages= ["useful"])


# def is_integer(s):
#     if len(s) == 0:
#         return False
#     if s[0] in ('+', '-'):
#         return s.lstrip('+').lstrip('-').rstrip().isdigit()
#     return s.strip().isdigit()
#
#
# print(is_integer('+34'))

# from datetime import datetime
#
#
# current_datetime = datetime.now().year
# print(current_datetime)


from datetime import datetime

# current_datetime = datetime.now()
#
# future_month = (current_datetime.month % 12)+1
# future_year = current_datetime.year + int(current_datetime.month / 12)
# future_datetime = datetime(future_year, future_month, 1)
#
# print(future_datetime )    # True


# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# ts = seventh_day_2020.timestamp()
# print(ts)   # 1578398400.0
#
# ts += 100000
# print(datetime.fromtimestamp(ts))  # 2020-01-08 17:46:40


from datetime import datetime

# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# # print(seventh_day_2020)
# print(seventh_day_2020.strftime('%A %d %B %Y')) # Tuesday 07 January 2020


s = '10 January 2020'
print(datetime.strptime(s, '%d %B %Y')) # 2020-01-10 00:00:00