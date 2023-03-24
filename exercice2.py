from math import sqrt


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


largeur = special_input("Largeur ? ", float, "x > 0")
hauteur = special_input("Hauteur ? ", float, "x > 0")
diagonale = sqrt(largeur ** 2 + hauteur ** 2)
print(f"Diagonale : {diagonale}")
