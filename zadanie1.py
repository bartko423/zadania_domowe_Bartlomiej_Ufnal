
#sprawdzanie czy jest rok przestępny

rok_prze = input("Podaj rok by sprawdzic czy jest przestepny")

if rok_prze.isdigit():
    if int(rok_prze) % 4 == 0 or 400 == 0:
        print("to jest rok przestepny")
    elif int(rok_prze) % 100 != 0:
        print("to nie jest rok przystępny")
else:
    print("podaj rok")