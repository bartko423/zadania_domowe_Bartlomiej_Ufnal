# gra kółko i krzyżyk
# użytkownik podaje stringa zawierającego X, O lub _ oznaczający puste miejsce
# należy sprawdzić czy wygrywa X, O czy nie ma wygranego

# dokończyć grę

# przyjac input od uzytkownika
dane = input("Podaj grę")
# sprawdzic czy string ma 9 znaków
if len(dane) == 9:
    # sprawdzę x poziomo
    if dane.index("XXX") == 0:
        #wygrana x
        print("Wygrał X")
    elif dane.index("x__x__x") == 0:
        print("Wygrał X")
else:
    print("remis")

dane.index