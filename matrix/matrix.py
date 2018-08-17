import random
import time

while True:
	line = ""
	for i in range(79):
		line = line+str(random.randrange(0,2))
	print(line)
	time.sleep(0.05)