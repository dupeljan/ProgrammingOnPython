def freq(s):
	dict = {}
	for a in s:
		if (a >= '1' and a <= '9'):
			if (dict.get(a) == None):
				dict[a] = 1
			else:
				dict[a] += 1
	return dict

def createPalindrom(s):
	stattistics = freq(s)
	sorted_statistics = {a:stattistics[a] for a in sorted(stattistics.keys())}
	left = ""
	right = ""
	mid = ('-1',0)
	for (a,b) in sorted_statistics.items():
		if b%2 == 0:
			left=left+a*(b//2)
			right=a*(b//2)+right
		elif(mid[0] == '-1'):
			mid = (a,b)
	return left + (mid[0]*mid[1]) + right

l = []
c = input("input: ")
l.append(c)
while (c != "0"):
	c = input("input: ")
	l.append(c)
print(createPalindrom(l))