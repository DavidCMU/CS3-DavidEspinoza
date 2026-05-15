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

    start=time.time()
    selctionSort(otherlist, listLength)
    print(f"selection sort time elapse: {time.time() - start}")

    start=time.time()
    bubbleSort(thislist, listLength)
    print(f"bubble sort time elapse: {time.time() - start}")

    start=time.time()
    insertionSort(otherlist2, listLength)
    print(f"insertion sort time elapse: {time.time() - start}")
    
    start=time.time()
    mergeSort(otherlist3, 0,listLength -1)
    print(f"merge sort time elapse: {time.time() - start}")
    
    start=time.time()
    quickSort(otherlist4, 0, listLength-1)
    print(f"quickSort sort time elapse: {time.time() - start}")

    start=time.time()
    sorted(otherlist5)
    print(f"python sort time elapse: {time.time() - start}" )


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
    for x in range(listLength):
        for y in range(listLength - x - 1):
            if randomlist[y] > randomlist[y + 1]:
                randomlist[y],randomlist[y+1] = randomlist[y+1], randomlist[y]
    return randomlist

def selctionSort(randomlist, listLength):
    for x in range(listLength):
        smallestIndex = x
        for y in range(x+1, listLength):
            if randomlist[y] < randomlist[smallestIndex]:
                smallestIndex = y
        randomlist[x],randomlist[smallestIndex] = randomlist[smallestIndex],randomlist[x]
    return randomlist

def insertionSort(randomlist, listLength):
    for x in range(1, listLength):
        y = x
        while y > 0 and randomlist[y - 1] > randomlist[y]:
            randomlist[y-1], randomlist[y] = randomlist[y], randomlist[y -1]
            y -= 1
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
    if start < end:
        midpoint = (start+end) //2

        mergeSort(randomlist, start, midpoint)
        mergeSort(randomlist, midpoint+1, end)
        merge(randomlist, start, midpoint, end)
    return randomlist

def quickSort(randomlist, start, end):
    if start < end:
        pivotPoint = partition(randomlist,start, end)
        quickSort(randomlist, start, pivotPoint -1)
        quickSort(randomlist,pivotPoint +1,end)
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