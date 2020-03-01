L = [[word for word in line.split()] for line in open("operations.txt")]
bankAccounts = {}
for words in L:
	if (words[0] == "BALANCE"):
		if (words[1] in bankAccounts):
			print(bankAccounts[words[1]])
		else:
			print("ERROR")

	if (words[0] == "DEPOSIT"):
		if not(words[1] in bankAccounts):
			bankAccounts[words[1]] = 0
			bankAccounts[words[1]] = bankAccounts[words[1]] + int(words[2])
		else:
			bankAccounts[words[1]] = bankAccounts[words[1]] + int(words[2])

	if (words[0] == "INCOME"):
		for client in bankAccounts.keys():
			if (bankAccounts[client] > 0):
				bankAccounts[client] += bankAccounts[client]//100 * int(words[1])

	if (words[0] == "WITHDRAW"):
		if not(words[1] in bankAccounts):
			bankAccounts[words[1]] = 0
			bankAccounts[words[1]] -= int(words[2])
		else:
			bankAccounts[words[1]] -= int(words[2])

	if (words[0] == "TRANSFER"):
		if not(words[1] in bankAccounts):
			bankAccounts[words[1]] = 0
			bankAccounts[words[1]] -= int(words[3])
		else:
			bankAccounts[words[1]] -= int(words[3])

		if not(words[2] in bankAccounts):
			bankAccounts[words[2]] = 0
			bankAccounts[words[2]] += int(words[3])
		else:
			bankAccounts[words[2]] -= int(words[3])
