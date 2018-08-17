import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Bag-Simulator by Prismary")
print("---------------------------")
print(" Bag-Simulator by Prismary")
print("---------------------------")

contents = []
try:
	readsave = open("bag.txt", "r")
	for line in readsave:
		contents.append(line.replace("\n", ""))
	readsave.close()
	print("Contents loaded.")
except:
	readsave = open("bag.txt", "x")
	print("[!] Save file not found, no contents loaded.")

def save(contents):
	save = open("bag.txt", "w")
	for item in contents:
		save.write(item+"\n")

print("\nAvailable commands: 'view', 'add', 'rename','remove', 'move', 'swap', 'empty'")
while True:
	cmd = input("\n>> ")
	
	if cmd.startswith("exit"):
		break

	elif cmd == "view":
		print("\nBag contents: \n-------------")
		for item in contents:
			print(item)
		print("-------------")

	elif cmd.startswith("add"):
		try:
			contents.append(cmd.split(" ")[1])
			save(contents)
			print("Successfully added "+cmd.split(" ")[1]+" to the bag.")
		except:
			print("[!] Please define the item's name.")

	elif cmd.startswith("rename"):
		try:
			pos = contents.index(cmd.split(" ")[1])
			contents.remove(cmd.split(" ")[1])
			contents.insert(pos, cmd.split(" ")[2])
			save(contents)
			print("Successfully renamed "+cmd.split(" ")[1]+" to "+cmd.split(" ")[2]+".")
		except:
			print("[!] Unable to rename "+cmd.split(" ")[1]+".")

	elif cmd.startswith("remove"):
		try:
			contents.remove(cmd.split(" ")[1])
			save(contents)
			print("Successfully removed "+cmd.split(" ")[1]+" from the bag.")
		except:
			print("[!] Unable to remove "+cmd.split(" ")[1]+" from the bag.")

	elif cmd.startswith("move"):
		try:
			pos = int(cmd.split(" ")[2])-1
			contents.remove(cmd.split(" ")[1])
			contents.insert(pos, cmd.split(" ")[1])
			save(contents)
			print("Successfully moved "+cmd.split(" ")[1]+" to position "+cmd.split(" ")[2]+".")
		except:
			print("[!] Unable to move "+cmd.split(" ")[1]+" to position "+cmd.split(" ")[2]+".")

	elif cmd.startswith("swap"):
		try:
			pos1 = contents.index(cmd.split(" ")[1])
			pos2 = contents.index(cmd.split(" ")[2])
			contents.remove(cmd.split(" ")[1])
			contents.insert(pos1, cmd.split(" ")[2])
			contents.remove(cmd.split(" ")[2])
			contents.insert(pos2, cmd.split(" ")[1])
			save(contents)
			print("Successfully swapped "+cmd.split(" ")[1]+" and "+cmd.split(" ")[2]+".")
		except:
			print("[!] Unable to swap "+cmd.split(" ")[1]+" and "+cmd.split(" ")[2]+".")

	elif cmd.startswith("empty"):
		print("[!] Are you sure you want to empty the bag? (y/n)")
		if input("") == "y":
			contents = []
			save(contents)
			print("Successfully emptied the bag.")

	else:
		print("[!] Unknown command.")