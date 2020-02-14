
def task1(n):
	res = []
	for i in range(100,1000):
		sum = 0
		for j in str(i):
			sum += int(j)
		if (sum == n):
			res.append(i)
	return res

def task2(a,b):
	res = []
	for i in range(a,b):
		invert = int(str(i)[::-1])
		if (invert == i):
			res.append(i)
	return res

def task3(l):
	res = 0
	col = 1
	for i in range(1,len(l)):
		if (l[i] == l[i-1]):
			col += 1
		elif (col > res):
			res = col
			col = 1
		else:
			col = 1
	return res

def task4(l):
	res = 0
	length = 1
	i = 1
	while (i < len(l)):
		while ((i < len(l)) and (l[i-1] <= l[i])):
			length += 1
			i += 1
		if (length > res):
			res = length
		i += 1
		length = 1
	return res

def task5(l):
	l1 = []
	res = len(l)
	for i in range(1,len(l)-1):
		if ((l[i] > l[i-1]) and (l[i] > l[i+1])):
			l1.append(i)
	for i in range(1,len(l1)):
		dist = l1[i] - l1[i-1]
		if (dist < res):
			res = dist
	return res

#print(task1(int(input("Input n : "))))

#print(task2(int(input("Input a : ")),int(input("Input b : "))))

#print("Input list3 : ")
#print(task3([int(s) for s in input().split()]))

#print("Input list4 : ")
#print(task4([int(s) for s in input().split()]))

print("Input list5 : ")
print(task5([int(s) for s in input().split()]))