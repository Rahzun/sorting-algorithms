#Selection Sort Algorithm

def selection_sort(data):

    for scanIndex in range(0, len(data)):

        minIndex = scanIndex

        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex

        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]

    print(data)

selection_sort([3, 2, 8, 6, 1, 5, 7])