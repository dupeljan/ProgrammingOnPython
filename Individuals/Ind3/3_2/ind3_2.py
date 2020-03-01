import numpy as np

SD = "Result2"

textSA = [Numbers for Numbers in open("SA.txt")]
textSB = [Numbers for Numbers in open("SB.txt")]
textSC = [Numbers for Numbers in open("SC.txt")]

maxLen = np.max([len(textSA),len(textSB),len(textSC)])
textSD = []

for i in range(0,maxLen):
	if (i < len(textSA)):
		textSD.append(textSA[i])
	if (i < len(textSB)):
		textSD.append(textSB[i])
	if (i < len(textSC)):
		textSD.append(textSC[i])

f = open(SD+".txt","w")
for line in textSD:
	f.write(line)