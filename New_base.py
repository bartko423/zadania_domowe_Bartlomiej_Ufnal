
# jako argument domyślny dajemy typ zmienny - listę
#def dodaj_imie(imie, imiona=[]):
    #imiona.append(imie)
    #eturn imiona

# wywołujemy funkcję, bez podawania argumentu domyślnego
lista_imion = dodaj_imie("Ola")
print(lista_imion)

# okazuje się, że kolejne wywołanie funkcji dodaje imie do
# listy utworzonej przy pierwszym wywołaniu
#lista_imion2 = dodaj_imie("Ala")
#print(lista_imion2)

#lista_imion3 = dodaj_imie("Piotrek")
#print(lista_imion3)


 slownik = {'imiona': ['jacek', 'mati', 'bartek', 'aga'], 'nazwiska': ['pietruksza', 'ziemniak', 'skobelek', 'cyc']}

 slownik['imiona'].append('kama')

 print slownik
{'imiona': ['jacek', 'mati', 'bartek', 'aga', 'kama'], 'nazwiska': ['pietruksza', 'ziemniak', 'skobelek', 'cyc']}

In [4]: slownik['imiona'].delete('kama')

slownik['imiona'].remove('kama')

print slownik
{'imiona': ['jacek', 'mati', 'bartek', 'aga'], 'nazwiska': ['pietruksza', 'ziemniak', 'skobelek', 'cyc']}

print slownik['imiona'][0]
jacek

print slownik['nazwiska'][0]
pietruksza

print slownik['imiona'][0] slownik['nazwiska'][0]
  File "<ipython-input-9-5ebfbf4e3907>", line 1
    print slownik['imiona'][0] slownik['nazwiska'][0]
                                     ^
SyntaxError: invalid syntax


print slownik['imiona'][0], slownik['nazwiska'][0]
jacek pietruksza

 if 'jacek' in slownik['imiona]:
    if 'jacek' in slownik['imiona]:
                                  ^

if 'jacek' in slownik['imiona]:
    if 'jacek' in slownik['imiona]:



if 'jacek' in slownik['imiona']:
    slownik['imiona'].remove('jacek')

print slownik


slownik['imiona'].append('kama')

if 'kama' in slownik['imiona']:
    slownik['imiona'].remove('kama')
 print slownik






