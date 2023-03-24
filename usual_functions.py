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

# usrInput = specialInput("Enter a number: ", int, "x > 0")
# print(usrInput)
