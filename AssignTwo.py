#Simon Rosner
#1/22/2016
#This program calculates weekly pay and
#calculates the hypotenuse of a right triangle

import math #needed for math.sqrt
rate = int(input("Please enter hourly rate: "))
hours = int(input("Please enter hours worked: "))
print("Weekly pay: $",rate*hours)

firstLeg = int(input("Length of first leg: "))
secondLeg = int(input("Lenght of second leg: "))
print("Hypotenuse: ",math.sqrt((firstLeg**2)+(secondLeg**2)))
