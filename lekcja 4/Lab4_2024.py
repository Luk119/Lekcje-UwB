import os  ## moduł obsługi plików, katalogów, dysków

'''
Uwaga: wymienione w przykładach nazwy katalogów i plików
nie występują w Twoim PC-cie, dostosuj ich nazwy do istniejących !!!
Jeśli korzystasz z replit-a .... ścieżkę rozpocznij od "/home"

Operacje na plikach i katalogach:
aby zmieniać, tworzyć katalogi, oglądać ich zawartość itp. będziemy stosować funkcje
i metody z bibioteki o nazwie os, ta biblioteka ma szereg metod, każda metoda umożliwia
zrealizowania pewnych operacji na katalogach. Zapoznaj się z przykładami metod poniżej
a następnie wykonaj zadania
'''
######################## Obsługa dysków i folderów
### Przykład 1
## Metoda getcwd() pozwala sprawdzić jaką ścieżkę ma bieżacy folder, czyli ten w którym
## znajduje się Twój plik z programem

# moj_obecny_folder = os.getcwd()
# print(moj_obecny_folder)

### Przykład 2
### metoda listdir('.') służy do sprawdzania zawartości katalogu

# zawartosc_biezacego_folderu = os.listdir('.')
# print(zawartosc_biezacego_folderu)

### Przykład 3
### listdir('ścieżka dostępu do folderu') - zawartosc_konkretnego_folderu

# zawartosc_wskazanego_folderu = os.listdir('c:\\Windows')
# print(zawartosc_wskazanego_folderu)

### Przykład 4
# print(os.getcwd())   # sprawdzamy jaki jest nasz katalog roboczy/bieżący
# zmiana_katalogu_roboczego = os.chdir('c:\\Users') # zmiana bieżącego katalogu dyskowego na inny np. c:/Users
# print(os.getcwd()) # sprawdzamy jaki jest roboczy po wywołaniu instrukcji zmiany

### Przykład 5 - Filtrowanie nazw plików i katalogów według określonego wzorca
import fnmatch

'''
fnmatch - moduł umożliwiający wyszukiwanie określonych ciągów znaków,
zapewnia obsługę symboli wieloznacznych.
funkcja o takiej samej nazwie jak moduł fnmatch(nazwa, wzorzec) sprawdza czy podana
nazwa (typ String) zaczyna i/lub kończy się na określony wzorzec (typ String)
'''
# zdanie = 'Python to jezyk programowania.py'
# czy_to_prawda1 = fnmatch.fnmatch(zdanie,'P*a') # czy zmienna zdanie zaczyna się na literę P i kończy na m?
# print(czy_to_prawda1)
# czy_to_prawda2 = fnmatch.fnmatch(zdanie,'*.py') # czy zmienna zdanie kończy na m?
# print(czy_to_prawda2)

### Przykład 6
'''
Metoda makedirs() służy do tworzenia nowego folderu w bieżącym folderze
jeżeli folder istnieje to program wyrzuci błąd
'''
# os.makedirs('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa')

### Przykład 7
## Dołączanie pliku/katalogu i rozdzielenie ścieżki do folderu i nazwy wybranego pliku
# print(os.getcwd()) # sprawdzam nazwę folderu roboczego

## zmieniam miejsce "pobytu" przechodzę do katalogu o nazwie Dokument
# os.chdir('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa')

# moja_sciezka = os.getcwd()
# print(moja_sciezka) # ponownie sprawdzam gdzie się znajduję

## path.join łączy ciąg katalogów/pliku w ścieżkę
# nowa_sciezka = os.path.join(moja_sciezka,'Labo1.py')
# print(nowa_sciezka)

# rozdzielona_sciezka1 = os.path.split(os.path.realpath('Labo1.py')) # rozdzielam scieżkę i nazwę pliku
# print(rozdzielona_sciezka1)
# print(rozdzielona_sciezka1[0]) # pierwszy element z krotki
# print(rozdzielona_sciezka1[1])

### Przykład 8 - sprawdzanie rozmiarów plików (w bajtach)

# rozmiar_pliku = os.path.getsize('C:\\Users\\aneta\PycharmProjects\Programowanie1\L1.py')
# print(rozmiar_pliku)

### Przykład 9 - zmiana nazwy folderu
### Syntax: rename(stara_nazwa, nowa_nazwa)
# os.rename('C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa', 'C:\\Users\\aneta\PycharmProjects\Programowanie1\FolderNazwa2')
# print(os.listdir('C:\\Users\\aneta\PycharmProjects\Programowanie1'))

############################## Operacje  na plikach
'''
Zapoznaj się z możliwymi trybami zapisu do pliku:
http://programista-python.pl/operacje-wejscia-wyjscia-na-plikach-w-pythonie/
Tworzymy nowy plik tekstowy o nazwie: 'FirstFile.txt'
'''
### Przykład 10

## Syntax: open(file, mode)
## atrybut 'w': tryb zapisu, utwórz nowy plik lub nadpisz treść w pliku
# file1 = open('FirstFile.txt', 'w', encoding='utf-8')

# text1 = 'I love python,'
# file1.write(text1)  # zapis do pliku
#
# file1.close()  # operacja zamknięcia pliku

## Dodanie nowych danych do pliku
# file2 = open('FirstFile.txt', 'a', encoding='utf-8')  #  atrybut 'a':  tryb zapisu, dołącz treść
# text2 = ' very ... very much.'
# file2.write(text2)  # zapis do pliku
# file2.close()  # operacja zamknięcia pliku

## Odczyt zawartości
# file2 = open('FirstFile.txt', 'r')  #  atrybut 'r':  tryb odczytu (tryb domyślny)
# odczyt_tresci = file2.read()
# print(odczyt_tresci) # podgląd zawartości całego pliku

## Zapis i odczyt pliku kolejnych linii
# file11 = open('SecondFile.txt', 'w')  #  atrybut 'w':  tryb zapisu, utwórz nowy plik, lub nadpisz treść
# text11 = 'Mit o Prometeuszu, który poświęcił się dla ludzkości, wykradając bogom z Olimpu ogień\n \
#         Mit o Dedalu, praktycznym wynalazcy, i idealiście Ikarze, który leciał zbyt blisko słońca, stopił wosk swoich sztucznych skrzydeł i spadł\n\
#         Mit o Syzyfie skazanym na wieczne wtaczanie głazu, który przy samym szczycie znów spadał – stąd pojęcie syzyfowej pracy\n\
#         Mit o Narcyzie, który zachwycił się własną urodą\n\
#         Mity o Korze i Demeter\n\
#         Mit o jabłku niezgody i pięknej Helenie, o kowalu Hefajstosie i jego żonie Afrodycie\n\
#         Mit o Apollu i Marsjaszu, który ośmielił się współzawodniczyć z bogiem\n\
#         Mit o labiryncie i Tezeuszu, któremu udało się z niego wyjść dzięki podarowanemu mu przez Ariadnę kłębkowi nici\n\
#         Mit o Pigmalionie zakochanym w stworzonej przez siebie rzeźbie kobiety\n\
#         Mit o śpiewaku trackim Orfeuszu, który poszedł do podziemi po swoją żonę Eurydykę\n\
#         Mit o Amorze i Psyche\n\
#         Mit o Niobe, która straciła swoje dzieci z powodu własnej pychy\n'
#
# file11.write(text11)
# file11.close()

# Odczyt zawartości
# file3 = open('SecondFile.txt', 'r')  #  atrybut 'r':  tryb odczytu (tryb domyślny)
# print(file3.read())    # odczyt całości treści
# print(file3.readlines(1))    # odczyt 1 linii

###  odczyt linia po linii
# for linia in file3:
#    print(linia)

# ########## Szybki zapis i odczyt danch - picle
'''
moduł picle służy do utrwalania, zapisywania i odczytywania dowolnych obiektów Pythona.
Tego typu obiekty są nazywane trwałymi (ang.persistent) a plik je przechowujący
pamięcią trwałą (persistent storage). Zakończenie programu nie powoduje bowiem ich zniknięcia.
'''
import pickle

### Przykład 11
## zapis danych do pliku
# filename = 'lista_zakupow.data'
# products = ['jabłka', 'ziemniaki', 'pomidory']
# f1 = open(filename, 'wb')
# pickle.dump(products, f1)
# f1.close()


## usunięcie zmiennej z pamięci i ponowne wczytanie danych
# del products
# # odzyskanie zmiennej
# f2 = open(filename, 'rb')
#
# products = pickle.load(f2)
# for rzecz in products:
#     print(rzecz)

### Przykład 12  - zapisywanie większej liczby obiektów
# products1 = 'jabłka'
# products2 = 'ziemniaki'
#
# f3 = open('myfile.pickle', 'wb')
# pickle.dump((products1,products2), f3)  # zapisujemy obiekty do krotki
# f3.close()
## Uwaga!: bez wywwołania metody .close() dane zostaną zapisane automatycznie najpóźniej
## w momencie zakończenia programu

# del products1, products2
## odzyskanie zmiennej
# f4 = open('myfile.pickle', 'rb')
# products = pickle.load(f4)  # przypisujemy wczytane obiekty do zmiennej
# print(products[0])
# print(products[1])

### Przykład 12  - funkcje pack(), unpack() w zapisie danych do pliku
'''
Jeśli chcemy zapisać dane inne niż tekst do pliku, możemy posłużyć się funkcją pakowania danych (pack)
z wbudowanego modułu struct. Zamienia ona tekst na dane binarne (w takiej postaci jak przechowywane są w
pamięci komputera). Generalnie, struct służy do obsługi danych binarnych przechowywanych w plikach,
bazie danych lub z połączeń sieciowych itp.
'''
from struct import *

'''
Dodatkowe informacje o funkcji pack(), pierwszy argument pack()
zawiera kolejne typy danach które mają być pakowane tj.
?: boolean
h: short int
l: long int
i: int
f: float
q: long long int
'''
# var = pack('hhl', 50, 100, 150)  # Zwróć uwagę że kolejne dane są zapisywane do krotki
# print(var)
# print(unpack('hhl', var))

## Wariant z zapisem do pliku + pack()
# f1 = open('plik2.dat','wb') # litera b oznacza zapis danych binarnych
# number2 = pack('h',9876)
# f1.write(number2)
# f1.close()

## Odczyt danych z pliku
# f2 = open("plik2.dat", "rb")   # litera b oznacza odczyt danych binarnych
# print(unpack('h',f2.read()))
# f2.close()


### Przykład 12 - użycie funkcji eval
'''
Syntax:  eval(expression, globals=None, locals=None)
globals,locals - opcjonalne  x = 10
'''
# x = 1
# y = eval(input('Podaj równanie prostej lub wielomianu: '))
# print(y)

########################## Zadanie 1 #########################
## Utwórz funkcję która będzie zmieniała bieżący katalog dyskowy na inny wskazany przez
## użytkownika (nazwa ścieżki do katalogu to argument wejściowy funkcji)
## oraz będzie wyświetlała zawartość wskazanego przez użytkownika katalogu.

# import os
#
# def zmiana_katalogu(sciezka):
#     try:
#         os.chdir(sciezka)
#         print(f"Zawartość katalogu {sciezka}:")
#         for plik in os.listdir():
#             print(plik)
#
#     except FileNotFoundError:
#         print("Podana ścieżka nie istnieje.")
#     except PermissionError:
#         print("Brak uprawnień dostępu do wskazanego katalogu.")


########################## Zadanie 2 #########################
## Korzystając z utworzonej funkcji napisz funkcję która będzie zmieniała bieżący katalog
## dyskowy na inny wskazany przez użytkownika oraz będzie wyświetlała zawartość wskazanego przez
## użytkownika katalogu.
## Przetestuj działanie programu dla natepującego przypadku:
## program działa tylko wówczas gdy użytkownik odpowie "yes" na pytanie:
## "Czy mam zmienić katalog?", zastosuj pętle while True(zmuś użytkownika :) do wpisania "yes")


# def pytanie_i_zmiana(sciezka):
#     while True:
#         pyt = input("Czy mam zmienić katalog? (yes - no)")
#         if pyt != "yes":
#             continue
#         else:
#             zmiana_katalogu(sciezka)
#             break
#
# sciezka = input("Podaj ścieżkę do katalogu: ")
# pytanie_i_zmiana(sciezka)

########################## Zadanie 3 #######################
## W swoim folderze roboczym (w którym masz plik programu) utworz folder o nazwie Dokument,
## do w/w folderu przekopiuj lub utwórz 3 dowolne pliki z rozszerzeniem *.doc np. (Lab1.doc, Lab2.doc, Lab3.doc)
## następnie wykonaj następujące zadania:
## a) korzystając z instrukcji Pythona wyświetl wszystkie pliki znajdujące się folderze roboczym
## b) korzystając z metod Pythona i (pętli lub funkcji filter) wyświetl tylko pliki z rozszerzeniem *.doc znajdujące się folderze roboczym

# python_dir = os.getcwd()
#
# nazwa_katalogu = "Dokumenty"
# dokumenty_path = os.path.join(python_dir, nazwa_katalogu)
# try:
#     os.mkdir(dokumenty_path)
# except FileExistsError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
#
# os.chdir(dokumenty_path)
# print(os.getcwd())
#
# with open("Lab1.doc", "w") as file:
#     pass
# with open("Lab2.doc", "w") as file2:
#     pass
# with open("Lab3.doc", "w") as file3:
#     pass
#
#
# print(os.listdir(".")) #bierzący folder
# print(os.listdir(dokumenty_path)) #folder dokumenty
#
# a = list(filter(lambda a: True if a.endswith(".doc") else False, os.listdir(".")))
# print(a)

########################## Zadanie 4 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze 2 katalogi:
## StudentDoc, StudentObrazy, do w/w folderów zapisz w każdym z nich 2 dowolne
## pliki odpowiednio tekstowe i graficzne, a następnie wyświetl zawartość poszczególnych
## folderów podaj rozmiar każdego pliku

# current_path = os.getcwd()
# print(current_path)
# stu_txt = os.path.join(current_path, "StudentDoc")
# stu_jpg = os.path.join(current_path, "StudentObrazy")
#
# try:
#     os.mkdir(stu_txt)
#     os.mkdir(stu_jpg)
# except FileExistsError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
#
# with open(os.path.join(stu_txt, "Tekst1.txt"), "w") as f:
#     pass
# with open(os.path.join(stu_txt, "Tekst2.txt"), "w") as f:
#     pass
# with open(os.path.join(stu_jpg, "Obraz1.jpg"), "w") as f:
#     pass
# with open(os.path.join(stu_jpg, "Obraz2.jpg"), "w") as f:
#     pass
#
# print(os.listdir(stu_txt))
# print(os.listdir(stu_jpg))
#
# print(os.path.getsize(os.path.join(stu_txt, "Tekst1.txt")))
# print(os.path.getsize(os.path.join(stu_txt, "Tekst2.txt")))
# print(os.path.getsize(os.path.join(stu_jpg, "Obraz1.jpg")))
# print(os.path.getsize(os.path.join(stu_jpg, "Obraz1.jpg")))


########################## Zadanie 5 #######################
## Korzystając wyłącznie z metod Pythona, utworz w swoim folderze katalog,
## a następnie zmień nazwę katalogu na inną, dowolną.

# curr_path = os.getcwd()
# try:
#     os.mkdir(os.path.join(curr_path, "Katalog"))
# except FileExistsError as e:
#     print(e)
#
# try:
#     os.rename(os.path.join(curr_path, "Katalog"), os.path.join(curr_path, "Katalog_zmiana"))
# except FileNotFoundError as e:
#     print(e)
########################## Zadanie 6 ########################
# # Utwórz trzy listy, zapisz, usuń a następnie odczytaj z pliku listy, użyj pickle

# import pickle
# lista1 = [1, 2, 3]
# lista2 = [2, 3]
# lista3 = [3]
#
# with open("task6.txt", "wb") as f:
#     pickle.dump([lista1, lista2, lista3], f)
#
# del lista1, lista2, lista3
#
# with open("task6.txt", "rb") as f:
#     lista1, lista2, lista3 = pickle.load(f)
#
# print(lista1, lista2, lista3)
#
# with open("task6.txt", "rb") as f:
#     print(*pickle.load(f))

########################## Zadanie 7 ########################
## Zapisz do pliku liczbę 123456789, spakuj, rozpakuj dane
## Sprawdź w dokumentacji pakietu struct typ danej
## https://docs.python.org/3/library/struct.html

# import struct
#
# number = 123456789
#
# with open('liczba.bin', 'wb') as file:
#     data = struct.pack('i', number)
#     file.write(data)
#
# with open('liczba.bin', 'rb') as file:
#     data = file.read()
#     number_unpacked = struct.unpack('i', data)[0]
#
# print(data)
# print("Liczba po odczycie:", number_unpacked)


########################## Zadanie 9 #########################
## Utwórz i zapisz do folderu 5 dowolnych plików tekstowych z dowolnym tekstem
##(więcej niż 5 zdań), możesz tez skopiować dowolny tekst.
## Nazwy plików: Tekst1ID_ABC, Tekst2ID_405.txt, Tekst3ID_607.txt, Tekst4ID_ABC.txt, Tekst5ID_DEF.txt
## Uwaga: pisząc program przyjmij założenie, że masz takich nazw plików w folderze tysiące,
## program ma działać niezależnie od liczby plików w folderze
## Utwórz funkcję która:
## a) odczyta z folderu nazwy wszystkich plików
## b) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmniej 3 liter.
## Utwórz dodatkowową funkcję która wykorzystując poprzednią funkcję sprawdzi:
## a) ile plików zawiera w identyfikatorze ID liczbę 0
## b) dla wszystkich plików które w nazwie nie mają liczby 0
##    wyznaczy liczbę słów
## c) dla plików zakończonych ciągiem znaków 'ABC' wyznacz liczbę wyrazów złożonych z conajmnie 3 liter.

# import os
#
# lista = ["Tekst1ID_ABC.txt", "Tekst2ID_405.txt", "Tekst3ID_607.txt", "Tekst4ID_ABC.txt", "Tekst5ID_DEF.txt"]
# current_path = os.getcwd()
# try:
#     os.mkdir(os.path.join(current_path, "Folder 5 plikow"))
# except FileExistsError as e:
#     print(e)
# katalog_path = os.path.join(current_path, "Folder 5 plikow")
# for i in lista:
#     with open(os.path.join(katalog_path, i), "w") as f:
#         f.write("""Skrzyżowanie, na którym pierwszeństwo przejazdu ustalają znaki.
#                    Uwaga! „Pierwszeństwo łamane”, ustalane przez znaki D-1 i A-7 z
#                    tabliczkami T-6, na której gruba linia wskazuje przebieg drogi z pierwszeństwem.""")
#
# def literki(path):
#     lista_plikow = os.listdir(path)
#     print(lista_plikow)
#     for i in lista_plikow:
#         if i.split(".")[0].endswith("ABC"):
#             licznik = 0
#             with open(os.path.join(path, i), "r") as f:
#                 tekst = f.read()
#                 for wyrazy in tekst.split(" "):
#                     if len(wyrazy) >= 3:
#                         licznik += 1
#                 print(f"plik '{i}' zawiera {licznik} wyrazów >= 3 litery.")
#     return lista_plikow
#
# def ID(path):
#     lista_plikow = literki(path)
#     licznik = 0
#     for i in lista_plikow:
#         if "0" in i.split(".")[0].split("ID_")[1]:
#             licznik += 1
#         if not "0" in i:
#             with open(os.path.join(path, i), "r") as f:
#                 tekst = f.read()
#                 print(f"ilosc wyrazow w pliku o nazwie {i}: {len(tekst.split(' '))}")
#
#     print(f"ID z liczbą 0: {licznik}")
# #c) już robi poprzednia funkcja
#
# literki(katalog_path)
# ID(katalog_path)