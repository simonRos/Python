#Simon Rosner
#1/22/2016
#Write a program that computes the future value of a savings account,
#Given the current value of the account,
#the annual interest rate, and assuming monthly compounding of interest.

value = float(input("What is the current value of the account? $"))
rate = float(input("What is the monthly interest rate? "))
months = int(input("How many months have passed? ")) #excpects percentage, not decimal
for x in range(0, months):
    value = value + (value * (rate/1200)) #calculation provided in prompt
    print("Month", x+1 ,": ",value)
