import random
import time

print("-- ZAHLENRATEN --\n")
max = int(input("Erraten wird eine Zahl von 0 bis "))
print("")
solution = random.randrange(1,max+1)

while True:
	guess = int(input("Deine Annahme: "))
	if solution	> guess:
		print(">> Die Zahl ist größer!\n")
	elif solution < guess:
		print(">> Die Zahl ist kleiner!\n")
	else:
		print("\n-- Die Zahl wurde erraten! --")
		break
time.sleep(5)