def driver():
    global pyramidArray
    global rowIndex
    global rowCount
    pyramidArray = []
    rowIndex = 1;
    print("Enter the number of rows ", end='')
    rowCount = input()
    #print(rowCount)
    buildPyramid(int(rowCount))
    printPyramid()
def buildPyramid(rc):
    for i in range(0, rc):
        newArray = []

        for j in range(i):
            newArray.append(1)
        pyramidArray.append(newArray)
def printPyramid():
    global pyramidArray
    global rowIndex
    global rowCount
    for i in range(0, int(rowCount)):
        for j in range(len(pyramidArray[i])):
            print(pyramidArray[i][j], end='')
        print("")
driver()
