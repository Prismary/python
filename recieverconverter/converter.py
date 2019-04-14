import os

root = "G:\Filme von Platte"


cmd = input("Zum ausführen bitte mit ENTER bestätigen. ")
index = os.listdir('.')
for i in index:
	dirname = i
	if "." in dirname:
		continue
	
	subindex = os.listdir(dirname)
	appends = len(subindex)-4
	if appends == 0:
		continue
	
	batchcontent = "copy /B \"{0}\{1}\REC.ts\"".format(root, dirname)
	for i in range(1,appends):
		batchcontent = batchcontent+"+\"{0}\{1}\REC.0{2}\"".format(root, dirname, i)
		
	batchcontent = batchcontent+" \"{0}\{1}.ts".format(root, dirname)+"\""
	
	with open("{}\convert.bat".format(dirname),"w") as bat:
		bat.write(batchcontent)