#Simon Rosner
#3/18/2016
#A short game for improving knowledge of US states
#The game does not make use of all of the methods in States.py

import States
import random

print ("[START]")

tooLong = True  #must be made false or game will progress
while tooLong:
    gameLength = int(input("How many questions would you like to answer? "))
    if gameLength > 50: #hard coded at 50 to avoid duplicates
        print("Please enter a number <= 50.")
    elif gameLength <= 0:
        tooLong = False
        gameLength = 0  #gameLength is reused later and cannot be < 0
    else:   #Duplicates are technically possible, they are unlikely
        tooLong = False
    
score = 0 #number of correct answers

for x in range (0, gameLength): #game runs gameLength number of times
    state = random.randint(0,49)    #random state is chosen
    trips = random.randint(1,3) #question is chosen
    if trips == 1:  #showcases first prompt method
        print("What is the abbreviation for ",States.getInfo(state,0),)
        answr = input("? ")
        if answr.lower() == States.nameToAbbrev(state).lower():
            score+=1
            print("Correct!")
        else:
            print("Incorrect!")   
    if trips == 2:  #showcases second prompt method
        print("What is the name for ",States.getInfo(state,1),)
        answr = input("? ")
        if answr.lower() == States.abbrevToName(state).lower():
            score+=1
            print("Correct!")
        else:
             print("Incorrect!")  
    elif trips == 3:    #showcases third prompt method
        print("What is the capital of ",States.getInfo(state,1),)
        answr = input("? ")
        if answr.lower() == States.abbrevToCap(state).lower():
            score+=1
            print("Correct!")
        else:
             print("Incorrect!")

    #adding more questions to showcase other methods is trivial

print("Total score: ", score,'/', gameLength) #display score
print("[GAME OVER]")

