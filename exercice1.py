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

distance = special_input("Distance ? ", float, "x >= 0")
time = special_input("Time ? ", float, "x > 0")
vitesse = distance / time

print(f"Vitesse : {vitesse}")