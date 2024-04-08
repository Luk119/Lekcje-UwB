def zdanie_rozdziel(tekst, rozdzielacz=",", pokaz_ilosc_fragmentow=True, pokaz_ilosc_wyrazow=True):
    zdania = tekst.split(".")

    if pokaz_ilosc_fragmentow == True:
        for zdanie in zdania:
            print(f"zdanie: {zdanie} ma {zdanie.count(rozdzielacz) + 1} '{rozdzielacz}'")
    if pokaz_ilosc_wyrazow == True:
        for zdanie in zdania:
            print("ilość wyrazów w podanym tekście: ", len(zdanie.split(" ")))
#     ¯\_(ツ)_/¯
#         ()
#        _/\_
