#Simon Rosner
#2/21/2016
#Use a Python dictionary to write a reverse phone spelling program.
#Given a phone number with characters in it,
#tell the user what the phone number is.
#For example, 800-USA-RAIL would return 800-872-7245
#and 814-641-TEXT would return 814-641-8398.

numDict = {'A': '2', 'B': '2', 'C': '2',
           'D': '3', 'E': '3', 'F': '3',
           'G': '4', 'H': '4', 'I': '4',
           'J': '5', 'K': '5', 'L': '5',
           'M': '6', 'N': '6', 'O': '6',
           'P': '7', 'Q': '7', 'R': '7', 'S': '7',
           'T': '8', 'U': '8', 'V': '8',
           'W': '9', 'X': '9', 'Y': '9', 'Z': '9'} #my dictionary

print("Enter a phone number letters in it.")
userInput = input("Please use all capital letters: ")#get input from user

for let in numDict:
    userInput = userInput.replace(let,numDict[let])#replace let w/ numDict[let]

print(userInput)#print result
