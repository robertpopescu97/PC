# Cu ajutorul celor invatate in ultima saptamana la curs se va realiza un calculator, astfel:
# - calculatorul detine cifre de la 0 la 9,
# - semnele matematice cu ajutorul carora se vor putea realiza operatii matematice sunt urmatoarele: + (adunare), - (scadere), / (impartire), * (inmultire)
# - pe langa cifrele amintite anterior si semnele matematice se va putea sterge cu ajutorul litere C
# - toate operatiile presupun interactiunea cu utilizatorul (functii de tip input)

print("""
Alegeti o operatie:
1. Adunare = +
2. Scadere = -
3. Inmultire = *
4. Impartire = /
""")

operatie_matematica = input("Introduceti operatia matematica:")
if operatie_matematica != int and \
        operatie_matematica not in range(5):
    print("Introduceti o cifra")
for x,y in range(10):
    if x != float:
        print('Introduceti o valoare de tip float')
        x = float(input())
    elif y != float:
        print('Introduceti o valoare de tip float')
        y = float(input())

elif num1 != float(input()) and num2 != (float(input)):
    print("Introduceti o cifra")
    if operatie_matematica == "1":
        num1 = input("Introduceti primul numar:")
        num2 = input("Introduceti al doilea numar:")
        adunare = num1 + num2
        print(f'Rezultatul adunari este = {adunare}')
    elif operatie_matematica == "2":
        num1 = input("Introduceti primul numar:")
        num2 = input("Introduceti al doilea numar:")
        scadere = num1 - num2
        print(f'Rezultatul scaderi este = {scadere}')
    elif operatie_matematica == "3":
        num1 = input("Introduceti primul numar:")
        num2 = input("Introduceti al doilea numar:")
        inmultire = num1 * num2
        print(f'Rezultatul inmultire este = {inmultire}')
    elif operatie_matematica == "4":
        num1 = input("Introduceti primul numar:")
        num2 = input("Introduceti al doilea numar:")
        impartire = num1 / num2
        print(f'Rezultatul impartire este = {impartire}')
