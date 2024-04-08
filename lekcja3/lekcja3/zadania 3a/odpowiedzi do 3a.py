# Task 1

# while True:
#
#     x = int(input("Podaj wartosc x:"))
#     y = int(input("Podaj wartosc y:"))
#
#     if x == 0 or y == 0:
#         print("Podana liczba jest zerem")
#         continue
#     else:
#         print(x*y)

# Task 2

# print("Łukasz Kundzicz")
# passwords = ("abc", "123")
# print(passwords)
# user_password = input("Podaj odpowiednie haslo:")
#
# if user_password == passwords[0]:
#     print("Niepoprawnie")
# elif user_password == passwords[1]:
#     print("Poprawnie")

# Task 3

# tab =[0] * 100
# from random import randint
#
# for i in range(0, 100):
#     tab[i] = int(randint(1, 100))
#     print(tab[i])
# tab.sort()
# for i in range(0, 100):
#     if tab[i] % 2 == 0:
#         print(tab[i], end=' ')

# Task 4

# print("Łukasz Kundzicz")
# passwords = ("abc", "123")
# print(passwords)
# user_password = input("Podaj odpowiednie haslo:")
#
# print("Niepoprawnie") if user_password == passwords[0] else print("Poprawna")

# Task 5

# funkcja = lambda x, y, z: x/y/z
# print(funkcja(12, 2, 2))

# Task 6

# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

# lista = ["Ł", "u", "k", "a", "s", "z"]
# funkcja = lambda cos: ''.join(cos)
# print(funkcja(lista))

# Task 7
# imie = "Łukasz Kundzicz"
#
# funkcja = lambda x: x.split()
# print(funkcja(imie))
#
# funkcja = lambda x: list(x)
# print(funkcja(imie))

# Task 8
# def litera(wyraz, a):
#     for i in wyraz:
#         if i == a:
#             return True
#     return False
#
# wyraz = "Społeczeństwo"
# x = "a"
# print(f"w wyrazie {wyraz} litera {x}: {litera(wyraz, x)}")

# Task 9

# login_list = []
# password_list = []
# users_dict = {}
#
# while(True):
#     login = input("Podaj login:")
#     if login == "STOP":
#         break
#     password = input("Podaj hasło:")
#     if password == "STOP":
#         break
#     login_list.append(login)
#     password_list.append(password)
#     users_dict[login] = password
#
# if len(login_list) < 1:
#     print("Brak danych w serwerze.")
# else:
#     print("Lista loginow:")
#     for i, p in enumerate(login_list, 1):
#         print(f"{i}. login - {p}")
#
#     print("Wszystkie dane:")
#     for l, p in users_dict.items():
#         print(f"{l} - {p}")

# Task 10
# moduł stars
# def Poziom(liczba_gwiazdek):
#     print("*" * liczba_gwiazdek)
#
# def Pion(liczba_gwiazdek):
#     for _ in range(liczba_gwiazdek):
#         print("*")
# import stars
#
# stars.Poziom(5)
# stars.Pion(1)
# stars.Poziom(4)
# stars.Pion(1)
# stars.Poziom(5)
# print("\n-----------------\n")
# stars.Pion(3)
# stars.Poziom(5)

#Task 11

#moduł sil

# def sn(x, y):
#     return silnia(x)/(silnia(y) * silnia(x-y))
# def silnia(x):
#     if x == 1 or x == 0:
#         return 1
#     else:
#         return x * silnia(x-1)

# import sil
#
# print(sil.sn(int(input("Podaj 1 liczbę:")), int(input("Podaj 2 liczbę:"))))
#
# print(sil.silnia(5)

#Task 12

# lista = list(range(1, 101))
# wynik = filter(lambda x: x % 2 == 0, lista)
#
# print(lista)
# print(",".join(map(str, wynik)))

# Task 13

# from functools import reduce
#
# lista = list(range(1, 101))
#
# multiplaction = lambda x, y: x * y
# suma = lambda x, y: x + y
# print("suma:", reduce(suma, lista))
#
# multiply = reduce(multiplaction, lista)
# print("multiply", multiply)

# Task 14

# results = []
#
# for i in range(2000, 3200):
#     if i % 7 == 0 and not(i % 5 ==0):
#         results.append(i)
#
# print("results:", results)

# Task 15
print("To to samo co poprzednie zadanie :^/")