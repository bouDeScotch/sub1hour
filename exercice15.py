def depense_totale(n, p):
	return 15*n + 22*p


def special_input(text, wantedType=str, condition="x==x"):
	isWright = False
	while not isWright:
		try:
			usrInput = wantedType(input(text))
			if eval(condition.replace("x", "usrInput")):
				isWright = True
		except:
			pass
	
	return usrInput


n = special_input("Nombre de DVD ?", int, "x > 0")
p = special_input("Nombre de livres ?", int, "x > 0")
print(f"{'' if depense_totale(n, p) >= 300 else 'pas '}plus de 300 €")