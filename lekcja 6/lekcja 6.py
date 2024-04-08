# #Task 1 Utwórz program kalkulator (dzielenie, pierwiastkowanie), wykonaj
# # obsługę wyjatków. Korzystając z assert sprawdź poprawność działania twojego kodu.
# def dzielenie(a, b):
#   try:
#     result = a / b
#   except ZeroDivisionError as e:
#     return (f"Error {e}")
#   else:
#     return result
#
# def pierwiastkowanie(a):
#   if a < 0:
#     raise ValueError("Nie ma pierwiastka z liczby ujemnej")
#   else:
#     return a ** 0.5
#   # try:
#   #   result = float(a ** 1/2)
#   # except ZeroDivisionError as e:
#   #   print(e)
#   # else:
#   #   return result

# print("Kalkulator\n1 - Dzielenie\n2 - Pierwiastkowanie\n")
# choice = int(input("Enter your choice: "))
# if choice == 1:
#   print("Dzielenie")
#   a = int(input("a: "))
#   b = int(input("b: "))
#   print(dzielenie(a, b))
#
# elif choice == 2:
#   print("Pierwiastkowanie")
#   a = int(input("a: "))
#   print(pierwiastkowanie(a))
# else:
#   print("Wrong choice")
#
# assert dzielenie(2, 2) == 1, "dzielenie Function error"
# assert pierwiastkowanie(4) == 2, "pierwiastkowanie Function error"

## Task 2 Utwórz program który na podstawie danych z pliku movies.csv, określi tytuł filmu czarno-białego z najwyższym
## budżetem, jego tytuł zapisze do pliku picle, wykonaj obsługę wyjatków (w tym FileNotFoundError).
## from google.colab import drive
## drive.mount('/content/drive')

# # Task 3 Utwórz funkcję licz(fun) która obliczy pierwiastki równania kwadratowego ax^2+bx+c = 0 dla dowolnych a,b,c
# # Wymagania:
# #
# # wykonaj obsługę wyjatków
# # argument wejściowy funkcji (fun) jest typu string np. '2x^2+3'
# # korzystając z assert sprawdź poprawność działania funkcji Dane wejsciowe: x^2+4x-21 Wynik: 3 lub -7

# def root_squares(a: int, b: int, c: int) -> float:
#
#     """
#     function takes three arguments a, b, c of quadratic equations and returns roots of it
#
#     Args:
#       a(int): first number
#       b(int): second number
#       c(int): third number
#
#     Returns:
#       root/roots of quadratic equation
#     Raises:
#       ZeroDivisionError: if a == 0
#       ValueError if Delta < 0
#     """
#
#     try:
#         delta = b ** 2 - 4 * a * c
#         if delta < 0:
#             raise ValueError("Delta cannot be negative")
#
#         elif delta == 0:
#             x = -b + delta ** 0.5 / (a * 2)
#             return x
#
#         else:
#             x1 = (-b + delta ** 0.5) / (2 * a)
#             x2 = (-b - delta ** 0.5) / (2 * a)
#             return x1, x2
#
#     except ZeroDivisionError as e:
#         raise ValueError(f"a must be grater than 0, {e}")
#
# print(*root_squares(1, 4, -21))
# assert root_squares(1, 4, -21) == 3 or -7, "Function root_squares() does not run correctly"

#ooooooooooooooooooooooooooooooo
#oo!!!!!!!!!!!!!!!!!!!!!!!!!!!oo
#oo!!CAŁA ODPOWIEDZ DO ZAD 3!!oo
#oo!!!!!!!!!!!!!!!!!!!!!!!!!!!oo
#ooooooooooooooooooooooooooooooo

# import re
# def root_squares(funkcja: str) -> float:
#
#     """
#     function takes three arguments a, b, c of quadratic equations and returns roots of it
#
#     Args:
#         funkcja(str): function takes three arguments a, b, c as: "ax^2+bx+c"
#
#     Returns:
#       root/roots of quadratic equation
#     Raises:
#       ZeroDivisionError: if a == 0
#       ValueError if Delta < 0
#       ValueError if Nieprawidłowy format funkcji
#     """
#
#     try:
#         wzorzec = r'([+-]?\d*)x\^2\s*([+-]?\d*)x\s*([+-]?\d+)'
#         dopasowanie = re.match(wzorzec, funkcja)
#
#         if dopasowanie:
#
#             a, b, c = dopasowanie.groups()
#             if a == "":
#                 a = 1
#             else:
#                 a = float(a)
#
#             if b == "":
#                 b = 0
#             else:
#                 b = float(b)
#
#             if c == "":
#                 c = 0
#             else:
#                 c = float(c)
#
#             delta = b ** 2 - 4 * a * c
#
#             if delta < 0:
#                 raise ValueError("Delta cannot be negative")
#
#             elif delta == 0:
#                 x = -b + delta ** 0.5 / (a * 2)
#                 return x
#
#             else:
#                 x1 = (-b + delta ** 0.5) / (2 * a)
#                 x2 = (-b - delta ** 0.5) / (2 * a)
#                 return x1, x2
#
#         else:
#             raise ValueError("Nieprawidłowy format funkcji.")
#
#     except ZeroDivisionError as e:
#         raise ValueError(f"a can not be 0, {e}")
#
# print(*root_squares("x^2+4x-21"))
# assert root_squares("x^2+4x-21") == 3 or -7, "Function root_squares() does not run correctly"





# Task 4
# Utwórz funkcję wielu zmiennych wejściowych
#
# -   wykonaj obsługę wyjątków
# -   argumenty wejściowe funkcji to dane numeryczne które mogą stanowić:
#     sekwencja liczb lub 1 lista zawierająca liczby lub 1 słownik którego wartości to liczby)
# -   korzystając z assert sprawdź poprawność działania funkcji dla:
# Dane wejsciowe: 1,2,3,4
# Wynik: 3 lub -7

# def fun(*args)