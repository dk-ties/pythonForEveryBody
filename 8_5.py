fname = 'mbox-short.txt' #input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

mailList = list()
count = 0

fh = open(fname)
for lines in fh:
    lines.split()
    if 'From:' in lines:
        continue
    elif 'From' in lines:
        mailList.append(lines.split())

for address in mailList:
      count += 1
      print(address[1])
print("There were", count, "lines in the file with From as the first word")
