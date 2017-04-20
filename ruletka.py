# 5. ruletka: otrzymawszy liczbę, sprawdź czy jest ona:
#   czerwona czy czarna*
#   wysoka czy niska (do 18, od 18)
#   parzysta czy nieparzysta
#PARZYSTE TO CZARNE NIEPARZYSTE TO CZERWON




ruletka = int(input("Podaj liczbę"))

if ruletka % 2 == 0:
    print("Czarne pole a więc liczba parzysta")
else:
    print("Czerwone pole a więc liczba nieparzysta")
if ruletka >= 18:
        print("Jest to liczba wysoka")
elif ruletka <= 18:
        print("Jest to liczba niska")

