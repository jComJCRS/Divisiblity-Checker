#Divisiblity Checker

#Importing Modules
import time

#Title of the project
print("Divisiblity Checker\nVersion 1.2\n")

#Giving a break
time.sleep(1)

#This is a looped project
while True:
    #Defining a list to find prime numbers or composite numbers
    numlist = []
    #Asking user to enter the value, prints an error message when a non-numeric value is entered
    try:
        value = int(input("Enter number to find divisiblity: "))
    except ValueError:
        print("Not a numeral, Enter a numeral to find divisiblity\n")
    #Finding the divisiblity one by one
    for i in range(1, value + 1):
        if value % i == 0:
            #Prints the given value's possible divisible numbers
            print("Divisible by " + str(i))
            #Adding the values into the list to find the given value in variable value is a prime or a composite number
            numlist.append(i)
        #If the value entered is zero, then the program stops
        if value == 0:
            exit()
    #Prints a blank line
    print("")

    #Finding the given value is a prime or a composite number
    if len(numlist) > 2:
        print(str(value) + " is a Composite Number\n")
    else:
        print(str(value) + " is a Prime Number\n")
