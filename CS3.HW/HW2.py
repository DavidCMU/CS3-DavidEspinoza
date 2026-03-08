import random
import time
def main():


    thislist = randomNumbers()
    listLength = len(thislist)
    otherlist = thislist.copy()
    otherlist2 = thislist.copy()
    otherlist3 = thislist.copy()
    otherlist4 = thislist.copy()
    otherlist5 = thislist.copy()

    selctionList = selctionSort(otherlist, listLength)
    bubbleList = bubbleSort(thislist, listLength)
    insertionList = insertionSort(otherlist2, listLength)
    mergeList = mergeSort(otherlist3, 0,listLength -1)
    quickList = quickSort(otherlist4, 0, listLength-1)
    start=time.time()
    pythonList = sorted(otherlist5)
    end=time.time()
    elapse = end - start
    print(f"python sort sort time elapse: {elapse}" )


    #print(pythonList)
    #print(quickList)
    #print(mergeList)
    #print(insertionList)
    #print(selctionList)
    #print(bubbleList)
    

def randomNumbers():
    randomlist = []
    for x in range(0,100000):
        randomlist.append(random.randint(1, 10000))
    return randomlist

def bubbleSort(randomlist, listLength):
    start=time.time()
    for x in range(listLength):
        for y in range(listLength - x - 1):
            if randomlist[y] > randomlist[y + 1]:
                randomlist[y],randomlist[y+1] = randomlist[y+1], randomlist[y]
    end=time.time()
    elapse = end - start
    print(f"bubble sort time elapse: {elapse}" )
    return randomlist

def selctionSort(randomlist, listLength):
    start=time.time()
    for x in range(listLength):
        smallestIndex = x
        for y in range(x+1, listLength):
            if randomlist[y] < randomlist[smallestIndex]:
                smallestIndex = y
        randomlist[x],randomlist[smallestIndex] = randomlist[smallestIndex],randomlist[x]
    end=time.time()
    elapse = end - start
    print(f"selection sort time elapse: {elapse}" )
    return randomlist

def insertionSort(randomlist, listLength):
    start=time.time()
    for x in range(1, listLength):
        y = x
        while y > 0 and randomlist[y - 1] > randomlist[y]:
            randomlist[y-1], randomlist[y] = randomlist[y], randomlist[y -1]
            y -= 1
    end=time.time()
    elapse = end - start
    print(f"insertion sort time elapse: {elapse}" )
    return randomlist

def merge(randomlist, start, midpoint, end):
        listSizeLeft = midpoint - start +1
        listSizeRight = end - midpoint
        
        leftList = [0] * listSizeLeft
        rightList = [0] * listSizeRight

        for x in range(listSizeLeft):
            leftList[x] = randomlist[start + x]
        for y in range(listSizeRight):
            rightList[y] = randomlist[midpoint + 1 + y]
        
        x =0
        y =0
        z = start

        while  x < listSizeLeft and y < listSizeRight:
            if leftList[x] <= rightList[y]:
                randomlist[z] = leftList[x]
                x+=1
            else:
                randomlist[z] = rightList[y]
                y+=1
            z+=1
        while x < listSizeLeft:
            randomlist[z] = leftList[x]
            x+=1
            z+=1
        while y < listSizeRight:
            randomlist[z] = rightList[y]
            y+=1
            z+=1

def mergeSort(randomlist, start, end):
    start=time.time()
    if start < end:
        midpoint = (start+end) //2

        mergeSort(randomlist, start, midpoint)
        mergeSort(randomlist, midpoint+1, end)
        merge(randomlist, start, midpoint, end)
    end=time.time()
    elapse = end - start
    print(f"merge sort time elapse: {elapse}" )
    return randomlist

def quickSort(randomlist, start, end):
    start=time.time()
    if start < end:
        pivotPoint = partition(randomlist,start, end)
        quickSort(randomlist, start, pivotPoint -1)
        quickSort(randomlist,pivotPoint +1,end)
    end=time.time()
    elapse = end - start
    print(f"quick sort time elapse: {elapse}" )
    return randomlist

def partition(randomlist, start, end):
    pivotValue = randomlist[end]
    index = start -1
    for x in range(start, end):
        if randomlist[x] < pivotValue:
            index += 1
            randomlist[index], randomlist[x]= randomlist[x], randomlist[index]
    randomlist[index +1], randomlist[end]= randomlist[end], randomlist[index+1]
    return index+1

    

main()