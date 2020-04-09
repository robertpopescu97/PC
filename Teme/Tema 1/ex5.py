afisaj = ("""
1. Lista de cumparaturi
2. Adaugare elemente
3. Stergere elemente
4. Stergere lista de cumparaturi
5. Cautare in lista de cumparaturi
""")

lista = 1
adaugare_elemete = 2
stergere_elemete = 3
stergere_lista = 4
cautare_lista = 5

lista = []
print(afisaj)
comanda_operator = (input(" Alegeti o cifra:"))

for a in range(1, 5):
    if a is comanda_operator:
        pass
else:
    print("Introduceti o valoare cuprinsa intre 1 si 5")

if int(comanda_operator) == 2:
    lista_cumparaturi = open("listacumparaturi.txt", "a+")
    produs = input('Introduceti produsle: ')
    if produs in open("listacumparaturi.txt").read():
        print(f' Produsul = "{produs.upper()}" cautat se afla deja in lista')
    elif produs != open("listacumparaturi.txt", "r").read():
        lista.append(produs)
        lista_adaugate2 = str(f"\n{produs}")
        lista_cumparaturi.write(str(lista_adaugate2))
        lista_cumparaturi.close()

elif int(comanda_operator) == 1:
    print(open("listacumparaturi.txt", 'r').read())

elif int(comanda_operator) == 3:
    print(open("listacumparaturi.txt", 'r').read())
    print("Vreti sa stergeti un element din lista?")
    raspuns = input(" Apasati Y/N:")
    if raspuns.upper() == "Y":
        print(open("listacumparaturi.txt", 'r').read())
        stergere = input("Introduceti elementul pe care vreti sa il stergeti: ")
        # segventa de stergerea  unei linii din lista
        with open("listacumparaturi.txt", "r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if stergere.lower() not in line:
                    f.write(line)
            f.truncate()
            f.close()
            if stergere not in open("listacumparaturi.txt", "r").read():
                print(f'Cuvantul introdus = "{stergere.upper()}" nu se afla in lista')
    elif raspuns.upper() == "N":
        print(afisaj)
    else:
        print('Va rog apasati Y/N')

elif int(comanda_operator) == 4:
    print(open("listacumparaturi.txt", "r").read())
    print(" Vreti sa stergeti lista?")
    raspuns2 = input("Apasatu Y/N: ")
    if raspuns2.upper() == "Y":
        open("listacumparaturi.txt", "w")
        print("Lista a fost stearsa")
    elif raspuns2.upper() == "N":
        print(afisaj)
    else:
        print(" Va rugam apasati Y/N")

elif int(comanda_operator) == 5:
    (open("listacumparaturi.txt", "r").read())
    print("Cauta un element in lista")
    raspuns3 = input("Ce cuvant cautati: ")
    with(open("listacumparaturi.txt", "r")) as z:
        new_z = z.read()
        for line in new_z:
            z.close()
    if raspuns3 in new_z:
        print(f'Cuvantul cautat "{raspuns3.upper()}" se afla in lista')
    else:
        print(f'Cuvantul cautat "{raspuns3.upper()}" nu se afla in lista')




