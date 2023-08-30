fname =input("Enter file name: ")
fh = open(fname)
lst = list()
wordList = list()
returnList = list()
for line in fh:
    line.rsplit
    for words in line.split():
        wordList.append(words)
        #print(words)
for words in wordList:
    if words in returnList:
        continue
    else:
        returnList.append(words)

returnList.sort()
print(returnList)

"""     lst.append(line.split())

print(len(lst))
print('Here are the list with word: ', lst)
    
for words in lst:
    returnList.append(words.split())
    
print('And here are the returnList: ',returnList) """