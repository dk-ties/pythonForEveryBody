#IMPORTS
import re

sum = 0
totalNumbers = 0
numbersToSum = []

#ask for file to check
name = input("Enter file:")
if len(name) < 1:
    name = "py4e-data.dr-chuck.net_regex_sum_1827612.txt"
handle = open(name)
#litel throw each line in the file, find numbers, and append them to numberToSum
#Check for empty lines/non numbers line
for lines in handle:
    if len(re.findall('[0-9]+',lines)) > 0:
        numbersToSum.append((re.findall('[0-9]+',lines)))
    
for num in numbersToSum:
    for x in num:
        sum += int(x)
        print(x)

print(sum)
