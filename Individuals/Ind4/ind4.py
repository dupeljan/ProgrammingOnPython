import os
import datetime

monthToHisNumber = {
	"январь" : 1,
	"февраль" : 2,
	"март" : 3,
	"апрель" : 4,
	"май" : 5,
	"июнь" : 6,
	"июль" : 7,
	"август" : 8,
	"сентябрь" : 9,
	"октябрь" : 10,
	"ноябрь" : 11,
	"декабрь" : 12,
}

myDateTime = input("Input date and time in format(dd.mm.yyyy HH:MM)\n")
infoMyDateTime = myDateTime.split()
myDate = infoMyDateTime[0].split('.')
myTime = infoMyDateTime[1].split(':')
myDateTime = datetime.datetime(int(myDate[2]),int(myDate[1]),int(myDate[0]),int(myTime[0]),int(myTime[1]))

dirWithCsvFiles = "CSV/Файлы/"

wordsAll = []
needIndex = -1
for csvFiles in os.listdir(dirWithCsvFiles):
	for line in open(dirWithCsvFiles + csvFiles):
		words = [word for word in line.split(',')]
		if words not in wordsAll:
			if "фамилия" not in words[0].lower():
				wordsAll.append(words)
			else:
				for i in range(len(words)):
					if "завершено" in words[i].lower():
						needIndex = i
wordsWithDate = []
for words in wordsAll:
	if (len(words[needIndex]) > 1):
		wordsWithDate.append(words[needIndex][1:-1])

res = []
print(myDateTime)
for i in range(len(wordsWithDate)):
	splitDateTime = wordsWithDate[i].split()
	date = splitDateTime[:-1]
	time = splitDateTime[len(splitDateTime)-1].split(':')
	thisDateTime = datetime.datetime(int(date[2]),monthToHisNumber[date[1].lower()],int(date[0]),int(time[0]),int(time[1]))
	if myDateTime > thisDateTime:
		print(i,wordsAll[i][0],wordsAll[i][1]," -: ",thisDateTime)
		res.append(wordsAll[i])

print(len(res))