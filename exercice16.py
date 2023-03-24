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

def distance(temps):
	if temps <= 2:
		return 90*temps
	else:
		return 90*2 + 120*(temps-2)
	
t = special_input("Temps de trajet (en heures) ? ", float, "x > 0")
print(f"Distance parcourue: {distance(t)} km")