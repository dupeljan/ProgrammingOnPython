text = [[word for word in line.split()] for line in open("ThisIsText.txt")]
res = []
for line in text:
	res.append("")
	for word in line:
		i = 1
		while(i<=len(word)):
			subString = word[0:i]
			reTouchedWord = word.replace(subString,"")
			if (len(reTouchedWord) == 0 or reTouchedWord == "." or reTouchedWord == "!"):
				word = subString + reTouchedWord
			i+=1
		res[len(res)-1] += " " + word
f = open("Result.txt","w")
for line in res:
	f.write(line + "\n")