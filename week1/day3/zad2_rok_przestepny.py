rok = input("Wprowadz rok:")
rok = int(rok)
if (rok%4 == 0 and rok%100!= 0) or rok%400==0:
    print("rok przestępny")
else:
    print("rok nieprzestępy")
