#Simon Rosner
#3/21/2016
#This program reads dollar amounts from a text file
#and writes a text file with equivelant pound and euro amounts

#constants
USDperGBP = 0.7 #Dollars per Pound
USDperEUR = 0.89#Dollars per Euro
inFile = "dolla.txt"    #name of input file
outFile = "out.txt" #name of output file

def convertToPound(money):  #returns equivelant pound amount
    return round(float(money)*float(USDperGBP),2)   #rounded to 2 dec place

def convertToEuro(money):   #returns equivelant euro amount
    return round(float(money)*float(USDperEUR),2)   #rounded to 2 dec place

f = open(inFile,"r")    #opens input file for read
for line in f:  #for each line in input file
    ou = open(outFile,'a')  #opens output file for append
    tempString = line   #store as tempString
    tempString = tempString.rstrip()    #strip newline
    x = line.replace('$','')    #remove dollar sign
    tempString += " \u00A3" + str(convertToPound(x)) #append pounds
    tempString += " \u20AC" + str(convertToEuro(x)) #append euros
    tempString += '\n'   #append newline
    ou.write(tempString)    #write tempString to output file 
    ou.close()  #close output file
f.close()   #close input file    
            
