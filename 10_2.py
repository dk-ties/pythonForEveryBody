name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
addresList =list()
timesList = list()
hoursList = list()
hoursCount = dict()
returnList = list()

for lines in handle:
    lines.split()
    if 'From:' in lines:
        continue
    elif'From ' in lines:
        addresList.append(lines.split())


for times in addresList:
    timesList.append(times[5])
    
#print(timesList)
for hours in timesList:
    hoursList.append(hours.split(':'))

#print(hoursList)
for hours in hoursList:
    hoursCount[hours[0]] = hoursCount.get(hours[0],0)+1

#Sorting the hoursCount

for Lort, pis in hoursCount.items():
    newTub = (Lort, pis)
    returnList.append(newTub)
returnList= sorted(returnList)
print('I got sorted')
for key, val in returnList:
    print(key, val)