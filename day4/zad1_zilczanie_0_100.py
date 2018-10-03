zakres = range(0, 100)
p = 0
n = 0

for liczba in zakres:
    if liczba % 2 == 0:
        p = p + 1
    else:
        n = n + 1
print("Liczba parzystych", p)
print("Liczba nieparzystych", n)

a="Liczba parzystych   " + str(p)
print(a)

a="Liczba parzystych    {}".format(p)
print(a)

a="Liczba parzystych {}. Liczba nieparzystych {}".format(p, n)
print(a)

a=f"Liczba parzystych {p}. Liczba nieparzystych {n}" #tzw. f sting
print(a)