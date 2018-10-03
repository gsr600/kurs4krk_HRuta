liczba = input("Wprowadz liczbę do sprawdzenia podzielnosci:")
war = liczba.isdigit()
if war == True:
    liczba =int(liczba)
    if liczba%3==0:
        print("Liczba jest podzielna przez 3")
    if liczba%5==0:
        print("Liczba jest podzielna przez 5")
    if liczba%7==0:
        print("Liczba jest podzielna przez 7")

else:
    print("To nie jest liczba")
