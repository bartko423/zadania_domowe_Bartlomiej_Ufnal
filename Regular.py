import re

input("wpisz miesiac")

sciezka = r'styczen|sobie'
dopasowanie = re.search(sciezka,)

if dopasowanie: #Sprawdzamy czy udalo sie cos znalezc
    numer = dopasowanie.group()
    print(numer)