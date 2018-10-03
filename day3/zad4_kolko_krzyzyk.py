#wynik = input("Wprowadz 9 znakowy wynik gry:")
wynik = "XOOOXXXOX"
if wynik[0]== wynik[1] and wynik[1] == wynik[2] and wynik[0] == wynik[2]:
    print("WIN")
    print(wynik[0])
elif wynik[3]== wynik[4] and wynik[4] == wynik[5] and wynik[3] == wynik[5]:
    print("WIN")
    print(wynik[3])
elif wynik[6] == wynik[7] and wynik[7] == wynik[8] and wynik[6] == wynik[8]:
    print("WIN")
    print(wynik[6])
elif wynik[0] == wynik[3] and wynik[3] == wynik[6] and wynik[0] == wynik[6]:
    print("WIN")
    print(wynik[0])
elif wynik[1] == wynik[4] and wynik[4] == wynik[7]:
    print("WIN")
    print(wynik[1])
elif wynik[2] == wynik[5] and wynik[5] == wynik[8]:
    print("WIN")
    print(wynik[2])
elif wynik[0] == wynik[4] and wynik[4] == wynik[8]:
    print("WIN")
    print(wynik[0])
elif wynik[2] == wynik[4] and wynik[4] == wynik[6]:
    print("WIN")
    print(wynik[2])
else:
    print("GAME OVER")
