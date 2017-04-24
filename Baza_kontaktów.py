#Baza danych


slownik = {'imiona': ['jacek', 'mati', 'bartek', 'aga'], 'nazwiska': ['pietruksza', 'ziemniak', 'skobelek', 'cyc']}

# Menu poleceń
choose_menu = ("Wybierz polecenie z listy: "
"\n dodaj imie wcisnij klawisz 1:"
"\n usun imie wcisnij klawisz 2: "
"\n wyswietl ilosc imion wcisnij kalwisz 3: "
"\n wyswietl imiona  wcisnij klawisz 4:"
"\n wyszukaj imie wcisnij klawisz 5:"
"\n zakoncz program wcisnij klawisz 0:\n")

print(choose_menu)

user_commannd = input()

#while True:
if user_commannd is '1':
    add_name = input("Podaj imie:")
    slownik['imiona'].append(add_name)
    print("Imię", add_name, "dodano do listy")

if user_commannd is '2':
    remove_name = input("Podaj imie")
    if slownik['imiona'].__contains__(remove_name):
        slownik['imiona'].remove(remove_name)
        print("Imię", remove_name, "usunięto z listy")
    else:
        print("Brak imienia na liscie")
#podaje ilosc imion na liscie
if user_commannd is '3':
    print("Ilosc imion na liście: ")
    print(slownik['imiona'].__len__())
#drukuje zawartość listy
if user_commannd is '4':
    print(slownik['imiona'])
""" wyszukuje imie w liscie  -> jeśli search_name zawiera sie w liscie imiona wydrukuj poszukiwane imie jesli nie
  wydrukuj brak imienia"""
if user_commannd is '5':
    search_name = input("Wyszukaj imie: ")
    if slownik['imiona'].__contains__(search_name):
        print("Imię", search_name, "jest na liście")
    else:
        print("Brak imienia na liście")
#zakończenie programu
if user_commannd is '0':
    print("Koniec Programu")









