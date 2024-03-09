import random
from time import time
import matplotlib.pyplot as plt


def traditionalBubbleSort(inArray):
    numIterations = len(inArray) - 1
    for i in range(numIterations):
        for j in range(numIterations):
            if inArray[j] > inArray[j + 1]:
                temp = inArray[j]
                inArray[j] = inArray[j + 1]
                inArray[j + 1] = temp


def modifiedBubbleSort(inArray):
    numIterations = len(inArray) - 1
    swapped = True
    start = 0

    while swapped:
        swapped = False

        for i in range(start, numIterations):
            if inArray[i] > inArray[i + 1]:
                inArray[i], inArray[i + 1] = inArray[i + 1], inArray[i]
                swapped = True

        if not swapped:
            break

        numIterations -= 1
        for j in range(numIterations - 1, start - 1, -1):
            if inArray[j] > inArray[j + 1]:
                inArray[j], inArray[j + 1] = inArray[j + 1], inArray[j]
                swapped = True

        start += 1


def benchmark():
    tradOutput = {'unsorted': [], 'mostlySorted': []}
    modOutput = {'unsorted': [], 'mostlySorted': []}

    for i in range(1, 11):
        unsortedList1 = []
        unsortedList2 = []

        k = i * 100
        for j in range(k):
            insert = random.randint(1, 10000)
            unsortedList1.append(insert)
            unsortedList2.append(insert)

        start_time = time()
        traditionalBubbleSort(unsortedList1)
        tradOutput['unsorted'].append(time() - start_time)

        start_time = time()
        modifiedBubbleSort(unsortedList2)
        modOutput['unsorted'].append(time() - start_time)

        mostlySortedList1 = unsortedList1
        mostlySortedList2 = unsortedList2
        if (k > 0):
            mostlySortedList1[k - 1], mostlySortedList1[k - 2] = mostlySortedList1[k - 2], mostlySortedList1[k - 1]
            mostlySortedList2[k - 1], mostlySortedList2[k - 2] = mostlySortedList2[k - 2], mostlySortedList2[k - 1]

            start_time = time()
            traditionalBubbleSort(mostlySortedList1)
            tradOutput['mostlySorted'].append(time() - start_time)

            start_time = time()
            modifiedBubbleSort(mostlySortedList2)
            modOutput['mostlySorted'].append(time() - start_time)
        else:
            tradOutput['mostlySorted'].append(0.0)
            modOutput['mostlySorted'].append(0.0)

    return tradOutput, modOutput


def showGraph(tradArray, modArray):
    plt.plot(range(1, 11), tradArray['unsorted'], label='Traditional BubbleSorting Unsorted')
    plt.plot(range(1, 11), tradArray['mostlySorted'], label='Traditional BubbleSorting Mostly Sorted')
    plt.plot(range(1, 11), modArray['unsorted'], label='Modified BubbleSorting Unsorted')
    plt.plot(range(1, 11), modArray['mostlySorted'], label='Modified BubbleSorting Mostly Sorted')
    plt.xlabel('Number of Samples (x100)')
    plt.ylabel('Time (s)')
    plt.title('Performance Comparison: Traditional vs. Modified Bubble Sort')
    plt.legend()
    plt.show()


list = [3, 2, 1]
print(list)
traditionalBubbleSort(list)
print(list)

list2 = [1, 2, 3]
print(list2)
modifiedBubbleSort(list2)
print(list2)

trad, mod = benchmark()
showGraph(trad, mod)
