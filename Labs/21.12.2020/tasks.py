def task1(n):
	if (n == 1):
		return "1"
	else:
		pred = task1(n-1)
		subStrings = [pred[0]]
		listStatistics = []
		for i in range(1,len(pred)):
			if (pred[i] == pred[i-1]):
				subStrings[len(subStrings)-1] += pred[i]
			else:
				subStrings.append(pred[i])
		for i in subStrings:
			listStatistics.append([str(i[0]),str(len(i))])
		res = ""
		for i in listStatistics:
			res = res + str(i[0]) + str(i[1])
	return res

print(task1(int(input("Input number : "))))