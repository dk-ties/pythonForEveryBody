largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
        except:
            print("Please enter a valid number.")
            continue
    print(num)
    if largest is None:
        largest = num
        
    if smallest is None:
        smallest = num
    print(largest, smallest)
    
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num

print("Maximum", largest)
print("Minimum", smallest)