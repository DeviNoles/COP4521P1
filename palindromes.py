#Devin Moure Assignment 1 COP4521 1/12/2021
#Problem #1 Palindromes
def driver():
    global paldict
    global palCount #instructioons start at 1
    palCount = 1
    paldict = {}
    inputString=""
    print("Enter the strings: ")
    while(inputString!="Done"):

        inputString = input()
        compareString = inputString.lower()
        compareString = compareString.replace(" ", "")
        #print(palCount)
        revString = compareString[len(compareString)::-1]
        isPalindrome(compareString, revString, inputString)
        #print(inputString)
        #print(compareString)
        #print(revString)

    print("The palindromes are: ")
    print(paldict)
def isPalindrome(compareString, revString, inputString):
    global paldict
    global palCount
    if(revString==compareString):
        paldict[palCount] = inputString
        palCount+=1
    else:
    #    print("FALSE")
driver()
