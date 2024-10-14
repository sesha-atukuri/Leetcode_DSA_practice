

def countchar(inputstr):
    cntDict = {}
    #inputstr = inputstr
    for char in range(len(inputstr)):
        #print(inputstr[char])
        if inputstr[char] in cntDict:
            cntDict[inputstr[char]] += 1
            #print(cntDict)
        else:
            cntDict[inputstr[char]] = 1

    print(cntDict)


countchar('banana')
