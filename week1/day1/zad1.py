#Blok nie wykonywany
#program sprawdza czy liczba65
#  jest podzielna przez 2

a = input("Proszę podaj wartość: ")     #wyświelta komuikat i po wprowadzeniu wartości w postaci str przypisuje ją do zmiennej a
b = int(a)                              #konwertuje str opsiiujacego liczbe a na wartośc liczbową int a i przypisuje pod zmienną b
c = b%2                                 #sprawdza czy wprowadzoena liczba jest podzielna przez 2 i czy zostaje reszta i przypisuje pod zmienna c
if c == 0:                              #sprawdza reszta z dzielenia jest równa 0
    print("liczba jest podzielna przez 2")
else:
    print("liczba nie jest podzielna przez 2")

""""
wielolinijkowy komentarz
poprzez potrojny cudzyslow
tak naprawde to jest string
"""