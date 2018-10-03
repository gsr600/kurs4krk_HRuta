#Program oblicza pola kwadratu lub trójkąta
print("Program oblicza pole kwadaratu lub trójkąta")
a = input("Podaj jaką figurę chcesz obliczyć (1-kwadrat, 2-trójkąt): ")
if (a == "1"):
        a = input("poadaj długość boku kwadratu a =  ")
        a = int(a)
        area = a**2
        print("pole kwadratu jest równe =", area)
elif (a == "2"):
        a = input("poadaj długość podstawy a =  ")
        h = input("podaj wysokość trójkąta h = ")
        a = int(a)
        h = int(h)
        area = 0.5*a*h
        print("pole trojkata równe jest =", area)
else:
        print("Zły wybór")