# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny


bok1 =int(input("Długość boku 1"))
bok2 =int(input("Długość boku 2"))
podstawa = int(input("długość podstawy"))

if bok1 + bok2 > podstawa:
    print("Trójkąt wykonalny")
    if bok1 + podstawa > bok2:
        print("Trójkąt wykonalny")
    if bok1 + podstawa > bok2:
        print("Trojkat wykonalny")
else:
    print("Trójkat niewykon")
if bok1 == bok2 and bok1 == podstawa and bok2 == podstawa:
    print("trojkat rownoboczny")
if bok1 != bok2 and bok1 != podstawa and bok2 != podstawa:
    print("trojkat rożnoboczny")
if bok1 == bok2 and bok1 != podstawa and bok2 != podstawa:
    print("trojkat równoramienny")
