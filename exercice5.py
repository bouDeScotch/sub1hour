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

def A(x):
	try:
		return 1/((x-1) * sqrt(x))
	except:
		return None


x = special_input("x ? ", float)
print("A(x)", "n'existe pas" if A(x) is None else "existe")
