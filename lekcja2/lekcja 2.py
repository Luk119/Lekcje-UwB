# Zadanie 1

# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1',
#                  'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                  'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1',
#                  'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                  'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC11',
#                  'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                  'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
# # for i in set_gene1 & set_gene2:
# #     print(i)
# print("a) intersection(część wspólna):", set_gene1.intersection(set_gene2.intersection(set_gene3)))
# print("b) intersection(część wspólna):", set_gene1 & set_gene2)
# print("c) difference:", (set_gene1 - set_gene2) - set_gene3)

# # Zadanie 2
#
# lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3', 'GALNT14', 'ERCC1',
#                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4', 'FGERA4']
# # for element in lista_gene1:
# #     if element == 'FGFR4':
# #         print(element, "należy do lista_gene1 na indeksie", lista_gene1.index(element))
# #     elif element == 'FGERA4':
# #         print(element, "należy do lista_gene1 na indeksie", lista_gene1.index(element))
# for i in range(0, len(lista_gene1)):
#     if lista_gene1[i] == 'FGFR4':
#         print(lista_gene1[i], "index:", i)
#     elif lista_gene1[i] == 'FGERA4':
#         print(lista_gene1[i], "index:", i)
# # Zadanie 3
#
# artykuł = """Emma i ja dostałyśmy instrukcje, by o 9:30 napisać o oficjalnych danych dotyczących zatrudnienia w Wielkiej Brytanii i wysłać nasze wersje do redaktora. Byłam przekonana, że Emma będzie ode mnie szybsza, ale miałam też szczerą nadzieję, że to ja będę lepsza.
#              Twórca Emmy, start-up o nazwie Stealth, nazywa ją „niezależną sztuczną inteligencją” zaprojektowaną, by świadczyć profesjonalne usługi, takie jak badania i analiza. Odkąd w modzie są prognozy, że sztuczna inteligencja (ang. artificial intelligence, AI) zastąpi pracowników biurowych, w tym również dziennikarzy, chciałam to sprawdzić na własnej skórze.
#              Emma rzeczywiście była szybka – dane wysłała w 12 minut. Mi zajęło to 35. Jej wersja była też lepsza, niż się spodziewałam. Fakty się zgadzały, zawarła nawet trafne treści, takie jak możliwość Brexitu (choć podzielała wątpliwą opinię, że wyjście z Unii Europejskiej byłoby niezwykle korzystne dla brytyjskiej gospodarki)."""
#
# print("Emma wystąpiło {} razy".format(artykuł.count("Emma")))
# ARTYKUŁ = artykuł.upper()
# words = artykuł.split(" ")
# var_sentences = artykuł.count(".")
# print("W tym tekście jest {} zdań.".format(var_sentences))
#
# # Zadanie 4
#
# user_number = int(input('Enter a number: '))
# if user_number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")
#
# # Zadanie 5
#
# punkty = int(input("Podaj liczbę uzyskanych punktów (0-15): "))
# print("Twoja ocena:")
# match punkty:
#         case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7:
#             print(2.0)
#         case 7 | 8 | 9:
#             print(3.0)
#         case 10:
#             print(3.5)
#         case 11:
#             print(4.0)
#         case 12 | 13:
#             print(4.5)
#         case 14 | 15:
#             print(5.0)
#         case _:
#             print("Niepoprawna liczba punktów")
#
# # Zadanie 6
# var_n = int(input('Enter n:'))
# result = 2
# for i in range(1,var_n+1):
#     result = result / (i+1 + 1)
# print('The result', result)
#
# # Zadanie 7
#
# from math import sqrt
# i = 1
# while i <= 10:
#     print("{}. {}".format(i, sqrt(i)))
#     i += 1
#
# # Zadanie 8
#
# from math import sqrt
#
# a = int(input("Enter A:"))
# b = int(input("Enter B:"))
# c = int(input("Enter C:"))
#
# if a == 0:
#     print("Nie można dzieluć przez zero")
# else:
#     delta = b ** 2 - 4 * a * c
#     if delta < 0:
#         print("brak rozwiązań.")
#     else:
#         x1 = (-b + sqrt(delta)) / (2 * a)
#         x2 = (-b - sqrt(delta)) / (2 * a)
#
#         print("x1 = ", x1)
#         print("x2 =", x2)
#
# # Zadanie 9
#
# tab = []
# for i in range(2, 1001, 2):
#     tab.append(i)
# print(tab)


# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print("Częćś wspólna a ^ b(intersection):", a.intersection(b))
# print("Suma a U b (union):", a.union(b))
# print("Różnica a - b (difference):", a.difference(b))
# print("Difference b - a:", b.difference(a))
# word = "Laboratoria1.py"
# print(word.endswith(".py"))
