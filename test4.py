from additionlogic import *

while True:

    try:
        n1 = input("Please enter the first integer: ")
        n1 = int(n1)
        n2 = input("Please enter the second integer: ")
        n2 = int(n2)
        break

    except ValueError:
        print("Invalid Input! Please try again ...")

    else:
        break



print("Lovely, you successfully entered two integers!")
AddIntegers(n1, n2)

SubtractIntegers(n1, n2)

