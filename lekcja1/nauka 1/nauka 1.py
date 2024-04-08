# #Zadanie 1
# list = ["Johnny", "Johnny", "Phil", "Sue", "Michael", "Luke", "Sue", "Peter", "Lois", "Christopher"]
# name = input("Type name:")
# print(name, "- index:", list.index(name))
# print("The word", name, "appeared", list.count(name), "times.")
# list.append("Grabsztynka")
# list.insert(3, "Sebek")
# list.sort()
# list.pop()
# list_2 = ["William", "John", "Sue"]
# list = list + list_2
# print(list)

# # Zadanie 2/3
# names = ["Jozin", "Dawid", "Julka"]
# surnames = ["Zbazin", "Szoka", "Ostaszewska"]
# ages = [54, 20, 21]
#
# person_info = {"name": names, "surname": surnames, "age": ages}
#
# person_number = int(input("Enter number(1-3):"))
#
# print("Person", person_number, ":")
# print("Name:", person_info["name"][person_number-1])
# print("Surname:", person_info["surname"][person_number-1])
# print("Age:", person_info["age"][person_number-1])
#
# fields = input("Enter university field:")
# person_info["field"] = fields
#
# print("field:", )
#
# #Zadanie 4
# print("Keys:", person_info.keys())
# j = 0
# for i in person_info.values():
#     j += len(i)
# print(j)

# ZADANIA DO WYKONANIA:
# # 1
# print("0 > 1:", 0 > 1)
# print("0 <= 1:", 0 <= 1)
# print("0 >= 1:", 0 >= 1)
# print("1 == 0:", 1 == 0)
# print("1 == 1:", 1 == 1)
# print("1 != 0:", 1 != 0)
# print("1 != 1:", 1 != 1)

# # 2
# var_x = float(input("Enter x value:"))
# var_y = float(input("Enter y value:"))
#
# print("2x + 5y =", 2 * var_x + 5 * var_y)

# # 3
# a = input("Enter name:")
# b = input("Enter surname:")
# c = input("Enter age:")
# d = input("Enter university field:")
# print("Jestem {} {} mam {} lat i studiuję {}".format(a, b, c, d))

# # 4
# print(1+2+10+20000001+4+347586970885, 321784560456434534646)
# print("1+2+10+20000001+4+347586970885 == 321784560456434534646:", 1+2+10+20000001+4+347586970885 == 321784560456434534646)

# # 5
# var_a = float(input("Enter a number: "))
# if var_a % 2 == 1:
#     print("Your number is odd.")
# else:
#     print("Your number is even.")

# # 6
# var_x = float(input("Enter x: "))
# var_y = float(input("Enter y: "))
#
# print("{} + {} = {}".format(var_x, var_y , var_x + var_y))
# print("{} - {} = {}".format(var_x, var_y , var_x - var_y))
# print("{} * {} = {}".format(var_x, var_y , var_x * var_y))
# print("{} / {} = {}".format(var_x, var_y , var_x / var_y))
# print("{} ^ {} = {}".format(var_x, var_y, var_x ** var_y))

# # 7
# x = float(input("Enter a number: "))
# print("(x > 1 and x < 13) -", (x > 1 and x < 13))
# print("(x != 5 or x < 0) -", (x != 5 or x < 0))

# # # # # # # Zadania dodatkowe:
# # 1/2

# name = input("Jak masz na imie? ")
# surname = input("Jak masz na nazwisko? ")
# age = input("Ile masz lat? ")
# food = input("Czy zdrowo się odżywiasz? ")
# sport = input("Czy lubisz sport? ")
# muzyka = input("Jakiej muzyki szłuchasz? ")
# kolor = input("Jaki jest twój ulubiony kolor? ")
# rodzenstwo = input("Czy masz rodzeństwo? ")
#
# if food.lower() == "tak":
#     food_ans = ""
# elif food.lower() == "nie":
#     food_ans = "nie"
#
# if sport.lower() == "tak":
#     sport_ans = "nie "
# elif sport.lower() == "nie":
#     sport_ans = ""
#
# if rodzenstwo.lower() == "tak":
#     rodzenstwo_ans = "ma rodzeństwo."
# elif rodzenstwo.lower() == "nie":
#     rodzenstwo_ans = "nie ma rodzeństwa."

# print(name + " " + surname + " ma " + age + " lat. Odżywia się bardzo" + food_ans + " zdrowo. Sport " + sport_ans + "jest mu obcy. Na codzień słucha muzyki " + muzyka + ", a jego ulubiony kolor to " + kolor + ". Na koniec warto dodać, że " + name + " " + rodzenstwo_ans)

# # # 3
# def generuj_sylabe(spolgloska):
#     samogloski = ['a', 'e', 'i', 'o', 'u']
#     sylaba = [spolgloska + samogloska for samogloska in samogloski]
#     return sylaba
#
# spolgloska = input("Wpisz spółgłoskę: ")
#
# sylaby = generuj_sylabe(spolgloska)
# print("Wygenerowane sylaby dla spółgłoski", spolgloska + ":")
# for sylaba in sylaby:
#     print(sylaba)

# pary = ["be", "ce", "ći", "de", "ef", "gie", "ha", "jot", "ka", "el", "em", "en", "pe", "er", "es",
#         "te", "wu", "y", "zet", "żet", "źet"]
# samogloski = ["a", "o", "u", "i", "e", "y"]
# spolgloska_user = input("Podaj spolgloske: ")
# if spolgloska_user in samogloski:
#     print("TO JEST SAMOGŁOSKA!")
# else:
#     for i in pary:
#         if spolgloska_user in i:
#             print(i)
# # # 4
# name = input("NAME: ")
# if name.lower() == "janusz" or name.lower() == "grażyna":
#     print(name, "To Janusz lub Grażyna.")
# else:
#     print(name, "to nie Janusz ani Grażyna.")
