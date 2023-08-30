text = "X-DSPAM-Confidence:    0.8475"

newText = text.strip()
colonFind = text.find('0')
textNumber = text[colonFind:len(text)]

print(float(textNumber))