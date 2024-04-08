# def func(a: int, b: float, c: int) -> float:
#     """
#
#     Args:
#         a(int): liczba
#         b(float): liczba
#         c(int): liczba
#
#     Returns:
#         wynik: suma 3 liczb
#     """
#     wynik = a + b + c
#     print(a + b)
#     print(a + c)
#     return wynik
#
#
# help(func)
# print(func.__doc__)
################## Dokumentacja  (docstrings) ########################################
################################################################################
#
# Dla zachowania czytelności i jednolitości kodu stosuj określoną gramatykę kodu, w pythonie
# najczęściej stosuje się konwencję opisaną w dokumencie PEP 258
# Wykonaj dokumentację kodu (dla funkcji, modułu)
# Stosuj obsługę wyjątków
import os
import re
# #################### Przykład 1 - dokumentacja funkcji (Google style)
# def divide(x: int,y: int) -> float:
#   """
#   Funkcja dzieli liczbę x przez liczbę y

#   Args:
#     x (int): dzielna
#     y (int): dzielnik

#   Returns:
#     wynik dzielenia x/y

#   """
#   result = x/y
#   return(result)

# print(divide(2,3))
# print(divide(x = 1, y = 2))
# help(divide)
# print(divide.__doc__)
################################################################################
################################################################################
######## Function: break() and continue()
################################################################################
## Funkcja break() jest używana często do zakończenia programu/pętli (for, while)
## podczas gdy funkcja continue() pozwala opuścić blok instrukcji
## i wrócić do początku pętli.

################### Example 1: the program only prints the numbers 0 1 2 3 4
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# licz = 0
# while licz in list_1:
#     print(list_1[licz]),
#     licz += 1  # licz = licz + 1
#     if licz >= 5:
#         break

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)

################################################################################
## Function with multiple arguments: args, kwargs
################################################################################

################################## Example 1:  sum of a sequence of numbers
# def suma(*args):
#     if not args:                        # case: no input parameters
#         return('no parameters')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


############# Example 2: Sum of arithmetic sequence
## functional requirements:
##  minimum number of input parameters: 1

# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

############  Example 3:   Sum the first four elements of arithmetic sequence
## functional requirements:
##  minimum number of input parameters: 4

# def sum2(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#
#      print(sumaLiczb)
#     return(None)
#
# sum2(1,2,3,4,5,6,7,8,9,10)
# sum2()

############  Example 3:   Sum the three elements
## functional requirements:
## minimum number of input parameters: 3
## user enter the name of input parameters

# def dict1(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# dict1(a=1, b=2, c=3)

############  Example 4: Say hello to a friend
## functional requirements:
## minimum number of input parameters: unknown
## name of input parameters: unknown

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# hallo(firstname="John", secondname='Smith')
# hallo(user="John")

############  Example 5: unpack list

# list_arg = [1, 3, 5]
#
# def unpack1(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# unpack1(*list_arg)
#####################################################
################################################################################
################################################################################


########################## Zadania do wykonania
# # ################################ Task 0
# '''
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line. Don't forget about function documentation
#
# '''
# ##### do testów możesz użyć:
# x = 1000
# y = 2101
# my_list = list(range(x,y,1))
# print(my_list)

# def div(x: int, y: int):
#     """
#
#     Args:
#         x(int): początek przedziału
#         y(int): koniec przedziału
#
#     Returns: nothing
#
#
#     """
#     lista = []
#     for i in range(x, y + 1):
#         if i % 7 == 0 and i % 5 != 0:
#             lista.append(str(i) + ".")
#     print(*lista)
#
# div(7, 21)

# # ################################ Task 1
## A website requires the users to input username and password to register.
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file
import os
from re import search
    # def ValidPassword(password):
    # # w while ma być wywołanie funkcji poprawić
    #     """
    #     fun checks if passwrd is correct or not:
    #     1. At least 1 letter between [a-z]
    #     2. At least 1 number between [0-9]
    #     3. At least 1 letter between [A-Z]
    #     4. Minimum length of transaction password: 4
    #     5. Maximum length of transaction password: 8
    #
    #     Args:
    #         password(string):
    #
    #     Returns:
    #         (bool): true - gdy hasło poprawne, false - gdy hasło niepoprawne
    #
    #     """
    #     if len(password) < 4 or len(password) > 8:
    #         print("Password must be at least 4 characters long and at most 8 characters long.")
    #         return False
    #     elif not re.search("[a-z]", password):
    #         print("Password must contain at least 1 letter between [a-z].")
    #         return False
    #     elif not re.search("[0-9]", password):
    #         print("Password must contain at least 1 number between [0-9].")
    #         return False
    #     elif not re.search("[A-Z]", password):
    #         print("Password must contain at least 1 letter between [A-Z].")
    #         return False
    #     else:
    #         print("Password is correct.")
    #         return True
    #
    # input_password = input("Enter your password: ")
    # while True:
    #     if ValidPassword(input_password):
    #         with open("Passwords.txt", "w") as file:
    #             file.write(f"{input_password} - Correct password")
    #             break
    #     else:
    #         input_password = input("Password ain't valid.\nEnter your password: ")
    #         continue

################ Task 2
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a
## single line.
## You should to document your code by using python docstrings
## (dokumentacja kodu styl google)
## Don't forget to handle exceptions (obsłudze wyjątków)
## Save result to *.pkl file use picle package
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#
# def div(x: int, y: int):
#     """
#
#     Args:
#         x(int): początek przedziału
#         y(int): koniec przedziału
#
#     Returns: nothing
#
#
#     """
#     lista = []
#
#     try:
#         for i in range(x, y + 1):
#             if i % 7 == 0 and i % 5 != 0:
#                 lista.append(str(i) + ".")
#         print(*lista)
#
#     except TypeError as e:
#         print(e)
#
# div(2, 21)

################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Name of input parameters:
## You should to document your code by using python docstrings (google)
###############

# def fun(*args):
#     """
#     Function which takes x1, x2, ... xn parameters and returns the pow(x1, x1), pow(x2, x2), ..., pow(xn) in list
#
#     Args:
#         *args(int): values
#
#     Returns:
#         list of pow(value, value)
#
#     """
#     if len(args) > 99:
#         raise TypeError("Arguments can't be grater than 99.")
#     lista = []
#     for i, num in enumerate(args, 1):
#         try:
#             globals()[f"x{i}"] = num ** num
#             lista.append(num ** num)
#         except TypeError as e:
#             print(e)
#
#     return lista
#
# print(*fun(1, 2, 3, 4, 5, 6))


################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3
## ....
## x1^x1, ... , x99^x99 if number of input parameters equals 99
## if number of input parameters equals greater than 100 will display an error message.
## Requirements:
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Don't forget to handle exceptions (obsłudze wyjątków)
###############
# def fun(*args):
#     """
#     Function which takes x1, x2, ... xn parameters and returns the pow(x1, x1), pow(x2, x2), ..., pow(xn) in list
#     Raise: number of args can't be grater than 99
#     Args:
#         *args(int): values
#
#     Returns:
#         list of pow(value, value)
#
#     """
#     if len(args) > 99:
#         raise TypeError("Arguments can't be grater than 99.")
#     lista = []
#     for i, num in enumerate(args, 1):
#         try:
#             globals()[f"x{i}"] = num ** num
#             lista.append(num ** num)
#         except TypeError as e:
#             print(e)
#
#     return lista
#
# print(*fun(1, 2, 3, 4, 5, 6))
########################## Task 5 ########################
## The first step,
## generate test data: create folder. Create 5 text files to this folder,
## each file contains more than 5 sentences.
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file
## contain words with more than 3 letters
## Next step: decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename
## b) if the file has 0 in the filename then the function counts words in the text of the file
## c) if the filename contains 'EF.txt', then the function copy this file to
## 'DocumentLab5copy' directory

import os
import shutil

main_path = os.getcwd()
new_file_name = "task5"
try:
    os.mkdir(os.path.join(main_path, new_file_name))

except FileExistsError as e:
    print(f"FIleExistsError {e} ")
file_names = ["Text1ID_ABC.txt", "Text2ID_405.txt", "Text3ID_607.txt", "Text4ID_ABC5.txt", " Text5ID_DEF.txt"]
os.chdir(os.path.join(main_path, new_file_name))
for i in file_names:
    with open(i, "w") as f:
        f.write(f"plik {i}. zawiera tekst. jakis tam. i saffsdfdsfds. sdfsdfsdf .sdf sdfsdfsdfsdf. sdfsdf")

os.chdir(main_path)


def doc(fun):
    def wrapper(*args):

        fun(*args)
        for path in args:
            ilosc_z_0 = 0
            if not os.path.isdir(path):
                raise FileNotFoundError("Nie ma takiego folderu")
            for file_name in os.listdir(f"{path}"):
                if file_name.endswith("EF.txt"):
                    try:
                        os.mkdir("DocumentLab5copy")
                    except FileExistsError as e:
                        print(f"FIleExistsError {e} ")
                    try:
                        shutil.copy(os.path.join(path, file_name), f"DocumentLab5copy/{file_name}")
                    except IOError as e:
                        print(f"IOError {e} ")

                if "0" in file_name:
                    ilosc_z_0 += 1
                    count = 0
                    with open(os.path.join(path, file_name), "r") as f:
                        count += len(f.read().split(" "))

                    print(f"ilosc wyrazow w {file_name}: {count}")
            print(f"W folderze {path} sa {ilosc_z_0} pliki ktore maja 0 w nazwie")

    return wrapper


@doc
def task5(*args):
    """
        takes path of files and prints how many words longer than 3 are in files
        that contains ABC in their name

    Args:
        *args (str): name of file

    Returns:
        nothing
    Raises:
        FileNotFoundError: if path is not found

    """
    for path in args:
        if not os.path.isdir(path):
            raise FileNotFoundError("Nie ma takiego folderu")

        print(os.listdir(f"{path}"))
        for file_name in os.listdir(f"{path}"):
            if "ABC" in file_name:
                count = 0
                with open(os.path.join(path, file_name), "r") as f:
                    for word in f.read().split(" "):
                        if len(word) > 3:
                            count += 1
                print(f"ilosc slow dlugosci ponad 3: {count}")

task5(os.path.join(main_path, new_file_name))