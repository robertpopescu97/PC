print("""
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
adaugare = []
comanda_operator = input(" Apasati o tasta:")
if comanda_operator.isalpha():
    print('Caractere introduse nu sunt permise')
elif int(comanda_operator) == 1:
    print(lista)
elif int(comanda_operator) ==2:
    lista = input('Introduceti produsle:')
#trebuie sa gasesto ceva ca sa salvezi inputurile




