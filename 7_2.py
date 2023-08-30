# Use the file name mbox-short.txt as the file name
totalLine = 0
count= 0
fname = "mbox-short.txt" #input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    fLine = line.split()
    floatLine = float(fLine[1])
    totalLine = totalLine + floatLine
    count += 1
avgLine = totalLine / count
print(f"Average spam confidence: {avgLine}")
