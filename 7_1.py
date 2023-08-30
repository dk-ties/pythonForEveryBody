# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
inp=fh.read()
upperInp = inp.upper()

print(upperInp.rstrip())
