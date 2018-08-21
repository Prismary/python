print("-- WORTUMKEHRER --")

def mirror(word):
	chars = []
	for i in range(0,len(word)):
		chars.append(word[i])
	chars.reverse()
	result = ""
	for item in chars:
		result = result+item
	return result
	
while True:
	word = input("Wort: ")
	print(">> "+mirror(word)+"\n")