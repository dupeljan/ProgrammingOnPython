def task1():
	col1 = int(input("Введите количество цветов 1го : "))
	L = []
	for i in range(col1):
		L.append(input("Input : "))		
	setA = set(L)
	L = []
	col2 = int(input("Введите количество цветов 2го : "))
	for i in range(col2):
		L.append(input("Input : "))
	setB = set(L)

	print("Пересечение :",setA & setB)
	print("Есть только у 1го :",setA - setB)
	print("Есть только у 2го :",setB - setA)

def task2():
	s1 = set()
	s2 = set()
	col1 = int(input("Введите количество школьников : "))
	for i in range(col1):
		print("Input:")
		ss = set([l for l in input().split()])
		if (s1 == set() and s2 == set()):
			s1 = ss
			s2 = ss
		else:
			s1 = s1 & ss
			s2 = s2 | ss;
	print("Хотя бы 1 : ",s2)
	print("Знают все : ",s1)

def task3():
	colDay = int(input("Input count day : "))
	colPart = int(input("Input count Parties : "))
	res = set()
	for c in range(colPart):
		start = int(input("Input start : "))
		break_ = int(input("Input break : "))
		i = 0
		while ((start + i*break_) <= colDay):
			if ((start + i*break_-6)%7 != 0 and (start + i*break_)%7 != 0):
				res.add(start + i*break_)
			i += 1
	print("Res = ",len(res))

#task1()
#task2()
task3()


