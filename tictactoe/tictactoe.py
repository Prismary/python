def print_board(tl, tm, tr, ml, mm, mr, bl, bm, br):

	print(tl+"|"+tm+"|"+tr)
	print("--+--+--")
	print(ml+"|"+mm+"|"+mr)
	print("--+--+--")
	print(bl+"|"+bm+"|"+br)

def write(player, choice):
	if choice == 7:
		return "tl"
	if choice == 8:
		return "tm"
	if choice == 9:
		return "tr"
	if choice == 4:
		return "ml"
	if choice == 5:
		return "mm"
	if choice == 6:
		return "mr"
	if choice == 1:
		return "bl"
	if choice == 2:
		return "bm"
	if choice == 3:
		return "br"

def blankcheck(choice,blank,tl,tm,tr,ml,mm,mr,bl,bm,br):
	isblank = False

	if choice == 7 and tl == blank:
		isblank = True
	if choice == 8 and tm == blank:
		isblank = True
	if choice == 9 and tr == blank:
		isblank = True
	if choice == 4 and ml == blank:
		isblank = True
	if choice == 5 and mm == blank:
		isblank = True
	if choice == 6 and mr == blank:
		isblank = True
	if choice == 1 and bl == blank:
		isblank = True
	if choice == 2 and bm == blank:
		isblank = True
	if choice == 3 and br == blank:
		isblank = True

	if isblank == True:
		return True
	else:
		return False

def wincheck(x, o, tl, tm, tr, ml, mm, mr, bl, bm, br):
	winplayer = ""
	if tl == x and tm == x and tr == x:
		winplayer = "x"
	elif ml == x and mm == x and mr == x:
		winplayer = "x"
	elif bl == x and bm == x and br == x:
		winplayer = "x"
	elif tl == x and ml == x and bl == x:
		winplayer = "x"
	elif tm == x and mm == x and bm == x:
		winplayer = "x"
	elif tr == x and mr == x and br == x:
		winplayer = "x"
	elif tr == x and mm == x and bl == x:
		winplayer = "x"
	elif tl == x and mm == x and br == x:
		winplayer = "x"

	if tl == o and tm == o and tr == o:
		winplayer = "o"
	elif ml == o and mm == o and mr == o:
		winplayer = "o"
	elif bl == o and bm == o and br == o:
		winplayer = "o"
	elif tl == o and ml == o and bl == o:
		winplayer = "o"
	elif tm == o and mm == o and bm == o:
		winplayer = "o"
	elif tr == o and mr == o and br == o:
		winplayer = "o"
	elif tr == o and mm == o and bl == o:
		winplayer = "o"
	elif tl == o and mm == o and br == o:
		winplayer = "o"

	if winplayer != "":
		win(winplayer)
		return True
	else:
		return False

def win(player):
	if player == "x":
		print("")
		print("------------------------")
		print(" Player X hat gewonnen!")
		print("------------------------")
	else:
		print("")
		print("------------------------")
		print(" Player O hat gewonnen!")
		print("------------------------")

blank = "  "
x = "><"
o = "()"

tl = blank
tm = blank
tr = blank

ml = blank
mm = blank
mr = blank

bl = blank
bm = blank
br = blank

print("----------------------------")
print(" Willkommen zu Tic-Tac-Toe!")
print("----------------------------")
print("Layout:")
print("")
print("7 8 9")
print("4 5 6")
print("1 2 3")
print("-------")
print("")
print_board(tl,tm,tr,ml,mm,mr,bl,bm,br)

while True:
	print("")
	while True:
		try:
			choice = int(input("Player X: "))
		except:
			continue
		if blankcheck(choice,blank,tl,tm,tr,ml,mm,mr,bl,bm,br) == True:
			exec(write("x", choice)+" = x")
			break
		else:
			print("Dieses Feld ist nicht verfügbar.")

	print("")
	print_board(tl,tm,tr,ml,mm,mr,bl,bm,br)
	if wincheck(x,o,tl,tm,tr,ml,mm,mr,bl,bm,br) == True:
		break

	print("")
	while True:
		try:
			choice = int(input("Player O: "))
		except:
			continue
		if blankcheck(choice,blank,tl,tm,tr,ml,mm,mr,bl,bm,br) == True:
			exec(write("o", choice)+" = o")
			break
		else:
			print("Dieses Feld ist nicht verfügbar.")
	
	print("")
	print_board(tl,tm,tr,ml,mm,mr,bl,bm,br)
	if wincheck(x,o,tl,tm,tr,ml,mm,mr,bl,bm,br) == True:
		break
