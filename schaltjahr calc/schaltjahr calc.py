def div(div, year):
	result = int(year)/int(div)
	sresult = str(result)
	try:
		if sresult.split(".")[1] != "0":
			return False
		else:
			return True
	except:
		return True
		
print("Bitte gib das zu überprüfende Jahr ein.")
while True:
	year = input("\n>> ")
	try:
		temp = int(year)
	except:
		print("[!] Die Eingabe ist keine Zahl.")
		continue

	if div(400, year) == True:
		print("Das Jahr ist ein Schaltjahr!")
	else:
		if div(4, year) == True and div(100, year) == False:
			print("Das Jahr ist ein Schaltjahr!")
		else:
			print("Das Jahr ist kein Schaltjahr!")