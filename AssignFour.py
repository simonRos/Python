#Simon Rosner
#2/1/2016
#This program simulates dice rolls and tracks them

import random #Needed for random module

def die (sides): #simulates a die roll
    return random.randint(1,sides);

def dice(sides,num): #simulates rolls with multiple dice
    total = 0
    for x in range (0,num): #dice per roll
            total=total+die(sides) 
    return total;

def diceSim(sides,num,rolls): #simulates multiple rolls
    tracker = [0]
    for x in range (0,sides*num): #list index created for each possible roll
                                #Indexes created for underrolls as well.
                                #Underroll indexes skipped in loops where applicable
        tracker.append(0)
    for x in range (0,rolls): # the rolls
        lastRoll = int(dice(sides,num))
        for x in range (num,len(tracker)): #Adds counts to the tracker.
            if lastRoll == x:
                tracker[x] = tracker[x]+1
    return tracker;

def AssignFour():   #interacts with the user.
    print ("[START]")
    #user input
    userSides = int(input("How many sides will the die/dice have?"))
    userNum = int(input("How many dice will be rolled on each roll?"))
    userRolls = int(input("How many rolls will be made?"))

    finalTracker = diceSim(userSides,userNum,userRolls) #Call to diceSim

    for x in range (userNum, len(finalTracker)): #displays total
        print("#",x,": ", finalTracker[x])
    #for the prompt:
    print("The number of rolls that resulted in a score of 7: ",finalTracker[7])
    print("[END]")
    
AssignFour() #run it
