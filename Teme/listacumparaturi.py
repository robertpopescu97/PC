"""
Lista cumparaturi:
                    - adaugare
                    - modificare
                    - stergere
                    - sortare

Pentru modificare sa specifice strimghul
"""

afisaj = ("""
1. Lista de cumparaturi
2. Adaugare elemente
3. Stergere elemente
4. Stergere lista de cumparaturi
5. Cautare in lista de cumparaturi
""")

#introducere produse

comanda_operator = input("Alegeti o operatie:")


if int(comanda_operator) == 2:
    lista_cumparaturi = open("cumparaturi,txt", "a+")
    produs = str(input("Introduceti produsul: ")).lower()
    pret = input("Introduceti pretul produsului: ")
    lista = []
    dictionar = {"produs": produs, "pret": float(pret)}
    lista.append(dictionar)

    for index, produse in enumerate(lista, 1):
            produs_adaugat = str(f'\n{index+1}. {produs} = {pret} Lei ')
            lista_cumparaturi.write(produs_adaugat)
    lista_cumparaturi.close()