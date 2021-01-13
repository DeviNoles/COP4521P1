def driver():
    global pyramidArray
    global rowIndex
    global rowCount
    pyramidArray = []
    rowIndex = 1;
    print("Enter the number of rows ", end='')
    rowCount = input()
    #print(rowCount)
    buildPyramid(int(rowCount)+1)
    printPyramid()
def buildPyramid(rc):
    for i in range(0, rc):
        newArray = []

        for j in range(i):
            if(i==1):
                newArray.append(1)
            elif(i==2):
                newArray.append(1)
            else:
                newArray.append(2)
        pyramidArray.append(newArray)
def printPyramid():
    global pyramidArray
    global rowIndex
    global rowCount
    for i in range(1, int(rowCount)+1):
        for j in range(len(pyramidArray[i])):
            print(pyramidArray[i][j], end='')
        print("")
driver()
