# Bubble Sort Algorithm

def bubble_sort(data):
    length = len(data)

    for iIndex in range(length):
        swapped = False

        for jIndex in range(0, length - iIndex - 1):

            if data[jIndex] > data[jIndex + 1]:
                data[jIndex], data[jIndex + 1] = data[jIndex + 1], data[jIndex]
                swapped = True

        if not swapped:
            break

    print(data)


bubble_sort([3, 2, 8, 6, 1, 5, 7])

