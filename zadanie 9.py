# 9. inupt - miesiąc oraz dzien,
#   okreslic pore roku
#21.03 wiosna#  ,
wiosna = 03.21
#22.06 lato ,
#23.09 jesien,
#22.12 zima

data = int(input("podaj miesiac"))
data2 = int(input("podaj dzien"))

if data >= 3 and data2 >= 21:
    print("wiosna")
    elif data >= 6 and data2 >= 22:
            print("lato")
    elif data >= 9 and data2 >=23:
            print("jesien")