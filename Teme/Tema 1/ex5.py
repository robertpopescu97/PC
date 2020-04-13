from typing import List

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

lista = [""]
print(afisaj)
comanda_operator = input(" Apasati o tasta:")
if comanda_operator.isalpha():
    print('Caractere introduse nu sunt permise')
elif int(comanda_operator) == 2:
    lista_cumparaturi = open("listacumparaturi.txt", "a+")
    produs = input('Introduceti produsle: ')
    lista.append(produs)
    lista_adaugate2 = str(f"\n{produs}")
    lista_cumparaturi.write(str(lista_adaugate2))
    lista_cumparaturi.close()
    with open("listacumparaturi.txt", "r") as f:
        for line in f.read():
            if produs not in line:
                print(f'Produsul introdus {produs.upper()}  se afla in lista"')
        f.close()
elif int(comanda_operator) == 1:
    print(open("listacumparaturi.txt", 'r').read())
elif int(stergere_elemete) == 3:
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
                if stergere not in line:
                    f.write(line)
                    f.truncate()
            print(f'Cuvantul "{stergere.upper()}" nu se afla in lista')
    elif raspuns.upper() == "N":
        print(afisaj)
    else:
        print("Va rog apasati Y/N")
