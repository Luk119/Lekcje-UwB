#Task 0
# import Rozprawka
#
# tekst = ["Odwiedź Piramidy w Gizie! To niezwykłe miejsce, gdzie przeszłość spotyka się z teraźniejszością.",
#          "Doświadcz tajemniczej atmosfery Machu Picchu w Peru, ukrytego wśród andyjskich gór.",
#          "Podziwiaj majestatyczne Wielkie Wodospady Iguaçu na granicy Brazylii i Argentyny."]
#
#
# def reklama(*args):
#     for arg in args:
#         Rozprawka.wspaniale()
#         print(arg)
#
# reklama(*tekst)
#
# Task 1

# from math import pow
# def funkcja(*args):
#     if len(args) == 1:
#         return pow(args[0], args[0])
#     elif len(args) == 2:
#         return pow(args[0], args[1])
#     else:
#         print("args ERROR")
#         return "args error"
# print(funkcja())



# Task 2

# def funkcja(tekst, *szukane_wyrazy):
#     if not szukane_wyrazy:
#         return "brak argumentów"
#     else:
#         i = 0
#         slowa_kluczowe = ["komputera", "skaner"]
#         wyrazy = tekst.split()
#
#         for slowo in wyrazy:
#             if slowo.lower() in slowa_kluczowe or slowo.lower() in szukane_wyrazy:
#                 i += 1
#         return i
#
# text = 'Wczytywanie do komputera tekstów, ilustracji, fotografii, itp. jest ' \
#        'możliwe dzięki urządzeniom zewnętrznym zwanym skanerami. Skaner to ' \
#        'urządzenie umożliwiające wprowadzenie do komputera grafiki i tekstu. ' \
#        'Dzięki zamianie skanowanej płaszczyzny na postać cyfrową może ona zostać ' \
#        'wyświetlona na ekranie monitora i zapisana na dysku w odpowiednim formacie ' \
#        'oraz może zostać poddana komputerowej obróbce. Skanery dzielimy na dwie podstawowe ' \
#        'grupy: ręczne (np. czytniki kodów paskowych) oraz stacjonarne. Najpopularniejszym ' \
#        'typem skanerów są skanery stacjonarne płaskie, które umożliwiają skanowanie ' \
#        'dokumentów o formacie A3 lub A4 i ich pochodnych. Są one podłączane do ' \
#        'komputerów przez port równoległy, uniwersalną magistralę szeregową lub sterownik SCSI.'
#
# wyrazy = ["są", "typem"]
#
# print(funkcja(text, *wyrazy))

#Task 3

# def arytmetyczna(*args):
#     if not args:
#         return "args ERROR"
#     else:
#         return sum(args) / len(args)
#
#
# import SredniaLiczb
#
# print("Srednia liczb: 1, 2, 3, 4, 5, 6 =", SredniaLiczb.arytmetyczna(2, 3, 4, 5, 6))

# Task  4

# from ZdanieRozdziel import zdanie_rozdziel
#
# text = """Była sobie dziewczyneczka, hop sa sa, hop sa sa. Szła dzieweczka do laseczka,
#            do zielonego, ha ha. Napotkała myśliweczka, hop sa sa. Tralala tralala."""
#
# zdanie_rozdziel(text, ".", True, True)

#moduł
# def zdanie_rozdziel(tekst, rozdzielacz=",", pokaz_ilosc_fragmentow=True, pokaz_ilosc_wyrazow=True):
#     zdania = tekst.split(".")
#
#     if pokaz_ilosc_fragmentow == True:
#         for zdanie in zdania:
#             print(f"zdanie: {zdanie} ma {zdanie.count(rozdzielacz) + 1} '{rozdzielacz}'")
#     if pokaz_ilosc_wyrazow == True:
#         for zdanie in zdania:
#             print("ilość wyrazów w podanym tekście: ", len(zdanie.split(" ")))
#brak zad 5
# Task 6

# from math import pow
# def a(n, a1 = 2, q = 1):
#     if n == 1:
#         return a1
#     elif n == 2:
#         return a1 * q
#     else:
#         return a1 * pow(q, n-1)
#
# def b(n, a1 = 1, q = 2):
#         return a1 * (1 - pow(q, n)) / (1 - q)


# from CiagGeometryczny import a, b
#
# print("an wyraz:", a(7, 3, 2))
# print("Suma:", b(10, 1, 3))

#Task 7

# def dostawa_towaru(liczba_pracownikow=5, **kwargs):
#     print(f"Liczba pracowników: {liczba_pracownikow}")
#     print("Dostarczone produkty:")
#     for produkt, ilosc in kwargs.items():
#         print(f"{produkt}: {ilosc}")
#         if produkt in baza_danych:
#             baza_danych[produkt].append(ilosc)
#         else:
#             baza_danych[produkt] = [ilosc]
#
# baza_danych = {}
# dostawa_towaru(pomarańcze=15, gruszki=500, jabłka=200)
# dostawa_towaru(10, pomarańcze=15, gruszki=50, jabłka=20, śliwki=10)
# print(baza_danych.items())
# print(baza_danych.keys())
# print(baza_danych.values())

# Task 8

# import pola
# import globals
#
# globals.a_kwadratu = 10
# globals.a_trojkata = 2
# globals.a_prostokata = 3
# print("trójkąt", pola.pole_figury("trójkąt"))
# print("prostokąt", pola.pole_figury("prostokąt"))
# print("kwadrat", pola.pole_figury("kwadrat"))

"""reszta w modułach pole_prostokata, pole_trojkata, pola, globals"""

#Task 9

# def dodaj_pole_kwadratu(func):
#     def wrapper(a, b=None):
#         if b is None:  # Sprawdzamy, czy drugi argument jest None
#             return a ** 2  # Jeśli tak, obliczamy pole kwadratu
#         else:
#             return func(a, b)  # W przeciwnym razie wykonujemy oryginalną funkcję
#     return wrapper
#
# @dodaj_pole_kwadratu
# def pole_prostokata(a, b):
#     return a * b
# @dodaj_pole_kwadratu
# def pole_trojkata(a, h):
#     return 0.5 * a * h
#
# # Dekorator dodający możliwość obliczenia pola kwadratu
#
# # Testujemy funkcje
# print("Pole prostokąta o bokach 3 i 4:", pole_prostokata(3, 4))
# print("Pole kwadratu o boku 5:", pole_prostokata(5))
# print("Pole trójkąta o podstawie 3 i wysokości 4:", pole_trojkata(3, 4))
# print("Pole kwadratu o boku 5:", pole_trojkata(5))

#Task 10
# def pole_trojkata(a, b):
#     return 0.5 * a * b
# def pole_prostokata(a, b):
#     return a * b
# def dekorator(func):
#     def wrapper(*args):
#         if len(args) == 2:
#             return args[1] * args[1]
#         else:
#             return func(*args)
#     return wrapper
# @dekorator
# def pole(figura, a, b):
#     if figura == "trojkat":
#         return pole_trojkata(a, b)
#     elif figura == "prostokat":
#         return pole_prostokata(a, b)
#
# print("Pole prostokata o boku 5 i 6:", pole("prostokat", 5, 6))
# print("Pole trójkąta o podstawie 3 i wysokości 4:", pole("trojkat", 3, 4))
# print("Pole kwadratu o boku 5:", pole("kwadrat", 5))

#Task 11

# def dekorator(func):
#     def wrapper(username, password, **kwargs):
#         zmienna = func(username, password)
#         zmienna.update(kwargs)
#         return zmienna
#     return wrapper
#
# @dekorator
# def logowanie(user = "edek2003", password = "Wsx123"):
#     return {"user": user, "password": password}
#
# print(logowanie(host = "www.google.com", port = "USB-C"))