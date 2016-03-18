#Simon Rosner
#1/22/2016
#This program allows you to enter a series of numbers
#and recieve the sum, product, and average of those numbers
print("Hello World") #moodle would only let me submit one file so I added this
count = int(input("How many numbers will you be entering? ")) #get count
total = 0 
product = 1 #starts as 1 to avoid math errors
for x in range(0, count):
    num = int(input("Enter a number: ")) #get input
    total = total + num #calc total
    product = product * num #calc product
#print statement. Average calculated in line.
print("Sum: ", total, " Product: ", product, " Average: ", total/count)
