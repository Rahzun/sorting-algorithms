
#Insertion Sort Algorithm

def insertion_sort(data):

    for scanIndex in range(1, len(data)):
        tmp = data[scanIndex]

        minIndex = scanIndex

        while minIndex > 0 and tmp < data[minIndex - 1]:
            data[minIndex] = data[minIndex - 1]
            minIndex -= 1

        data[minIndex] = tmp

    print(data)

insertion_sort([3, 2, 8, 6, 1, 5, 7])