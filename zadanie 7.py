# 7. po podaniu nazwy miesiaca, program napisze ilosc dni w miesiacu

M31 = ["styczeń","marzec","maj", "lipiec", "sierpien", "pazdziernik", "grudzien"]
M28 = ["luty"]
M30 = ["kwiecien", "czerwiec", "wrzesien", "listopad"]

miesiac = input("Podaj miesiac")

if miesiac in M28:
    print("28 dni")
elif miesiac in M30:
    print("30 dni")
elif miesiac in M31:
    print("31 dni")
