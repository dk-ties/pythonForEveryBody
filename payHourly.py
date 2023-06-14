#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.




hrs = float(input("Enter Hours: "))
rate = float(input("Enter payrate: "))


payout = 0

if hrs > 40:
    overTime = hrs - 40
    hrs = hrs - overTime
    payout = (hrs * rate)+ (overTime * (rate*1.5))
else: 
    payout = hrs*rate

print(payout)

""" 
def hourlyPay (rate, hrs):
    h = 0
    payout = 0
    while h < hrs :
        if h < 40:
            payout = payout + rate
            h = h+1
        else:
            rate = rate * 1.5
            payout =  payout + rate
    return(payout)


    
hourlyPay(hrs, rate)
print(payout)



# while timer < 40 payout = payout + rate timer = timer +1 """