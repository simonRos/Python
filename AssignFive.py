#Simon Rosner
#2/21/2016
#This program takes user input and returns the morse code equivelent.

dictionary = [("A",".- "),("B","-... "),("C","-.-. "),
    ("D","-.. "),("E",". "),("F","..-. "),
    ("G","--. "),("H",".... "),("I",".. "),
    ("J",".--- "),("K","-.- "),("L",".-.. "),
    ("M","-- "),("N","-. "),("O","--- "),
    ("P",".--. "),("Q","--.- "),("R",".-. "),
    ("S","... "),("T","- "),("U","..- "),
    ("V","...- "),("W",".-- "),("X","-..- "),
    ("Y","-.-- "),("Z","--.. ")]

print ("Please enter a string input ")  #get use input
userInput = input("(single word/phrase with no spaces and all alphabetic characters): ");

for x,y in dictionary:
    userInput = userInput.replace(x,y)  #replace x with y

print (userInput)   #print result
