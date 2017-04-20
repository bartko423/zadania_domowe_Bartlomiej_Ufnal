# 10. zamiana temperatury
#     wejscie: "35C" "100F"
#     wyjście "Temperatura w {typ} to {xxx} stopni"
#     C = (F - 32) * (5/9)
#     F = C * (9 / 5) + 32

wartosc = int(input("podaj temperature"))
jednostka = input("podaj jednostkę F lub C")
if jednostka is "C":
    print(wartosc * (9/5) + 32)
if jednostka is "F":
    print(wartosc - 32 * (5/9))