#Program zmienia wybrany n-ty znak na znak zdefiniowany w wybranym tekście
print("Program zmienia wybrany n-ty znak na znak zdefiniowany w wybranym tekście")
a = input("Wproawdz dowolny tekst: ")
print("Tekst ma", len(a), "zanków")
b = input("Wpisz n-ty numer litery do zmiany licząc od 0 i uwzględniając spacje: ")
b = int(b)
c = a[b]
print("Litera do zmiany to:",c)
print("Liczba liter szukanych w tekście:", a.count(c))
d = input ("Wpisz symbol znaku na jaki chcesz podmienić literę: ")
e = a.replace(a[b], d, 2)
print(e)
