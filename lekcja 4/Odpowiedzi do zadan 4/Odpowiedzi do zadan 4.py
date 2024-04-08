#Task 1
#import os
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

#Task 2

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

#Task 3

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

#Task 4
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

#Task 5
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

#Task 6
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
#Task 7
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

#Task 9

#import os
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






































import os
#
# os.mkdir("piesunek")
# os.rename("piesunek", "pesunek_new")

#Task 6

# import pickle
#
# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = [1,2,3,4,5,6,7,8]
# list3 = [1,2,3,4,5,6]
#
# with open("plik_pick.txt", "wb") as f:
#     pickle.dump([list1,list2,list3], f)
#
# del list1, list2, list3
#
# with open("plik_pick.txt", "rb") as f:
#     lista1, lista2, lista3 = pickle.load(f)
#
# print(lista1, lista2, lista3)

#Task 9

import os
def zawartosc_folderu(dir_path: str):
    print(f"Zawartosc folderu '{os.path.basename(dir_path)}': {os.listdir(dir_path)}")
    file_list = os.listdir(dir_path)
    for file in file_list:
        if file.endswith("ABC.txt"):
            licznik = 0
            with open(os.path.join(dir_path, file), 'r') as f:
                tekst = f.read()
                wyrazy = list(tekst.split(" "))
                for wyraz in wyrazy:
                    if len(wyraz) >= 3:
                        licznik += 1
            print(f"ilość wyrazów z conajmniej 3 literami w pliku {file}: {licznik}")

dir_path = os.path.join(os.getcwd(), "Pliki ze zdaniami")

try:
    os.mkdir("Pliki ze zdaniami")
except FileExistsError as e:
    print(e)

lista = ["Tekst1ID_ABC.txt", "Tekst2ID_405.txt", "Tekst3ID_607.txt", "Tekst4ID_ABC.txt", "Tekst5ID_DEF.txt"]


for filename in lista:
    with open(filename, "w") as file:
        file.write("""Badania nad wpływem kawy na zdrowie przynoszą mieszane rezultaty. Wiele badań sugeruje, że 
        umiarkowane spożycie kawy może być korzystne dla zdrowia. Kawa zawiera wiele związków, które mogą wpływać 
        korzystnie na funkcjonowanie organizmu. Jednak nadmierna konsumpcja kawy może prowadzić do negatywnych skutków,
        takich jak zaburzenia snu i podrażnienie żołądka. Dlatego ważne jest zachowanie umiaru w spożyciu kawy""")

zawartosc_folderu(dir_path)




