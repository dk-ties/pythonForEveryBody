fname = 'mbox-short.txt' #input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

mailList = list()
count = 0
whoSentMost = dict()

fh = open(fname)
for lines in fh:
    lines.split()
    if 'From:' in lines:
        continue
    elif 'From ' in lines:
        mailList.append(lines.split())
        
for address in mailList:
    whoSentMost[address[1]] = whoSentMost.get(address[1],0) +1

bigSender = None
bigNumber = None

for address, number in whoSentMost.items():
    if bigSender is None or bigNumber < number:
        bigSender = address
        bigNumber = number

print(bigSender, bigNumber)
