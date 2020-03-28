
import random
lista_cuvinte = ["Xilofon", "Alfabet", "Legume", "Anans", "Mazare",
				 "Caine", "Pisica", "Testament", "Virus", "Bere",
				 "Masina", "Piscina", "Kilogram", "Zarzavat",]
litere = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
		  "S", "T", "U", "V", "X", "Y", "Z"]
ghici = False
litere_folosite = []
incercari = 3
cuvant_ales = random.choice(lista_cuvinte).upper()
cuvant_de_ghicit = list(cuvant_ales)
print(cuvant_de_ghicit)
for i in range(len(cuvant_de_ghicit)):
	cuvant_de_ghicit[i] = "_"
print(' ' .join(cuvant_de_ghicit))
incercari_folosite = []

while not ghici and incercari > 0:
	litera_incercata = input(" Introduce o litera de la tastatura") .upper()
	if len(litera_incercata) == 1 and litera_incercata.isalpha():
		if litera_incercata in litere_folosite:
			print(" Ai incercat deja aceasta litera!", litera_incercata)
		elif litera_incercata not in lista_cuvinte:
			print(litera_incercata, "nu face parte din cuvant")
			incercari -= 1
			litere_folosite.append(litera_incercata)
		else:
			print(" Ai ghicit", litera_incercata)
			litere_folosite.append(litera_incercata)

	elif len(litera_incercata) == len(lista_cuvinte) and litera_incercata:
			print 
	else:
		print("")










