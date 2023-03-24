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


age = special_input("Age ? ", int, "x >= 0")
print("Majeur" if age >= 18 else "Mineur")
# if age >= 18:
# 	print("Majeur")
# else:
# 	print("Mineur")
