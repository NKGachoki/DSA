import sys

# Insertion sort algorithm
def InsertionSort(a):
    try:
        for i in range(1, len(a)):
            current_element = a[i]
            for j in range(i - 1, -1, -1):
                if a[j] > current_element:
                    a[j + 1], a[j] = a[j], current_element
                else:
                    a[j + 1] = current_element
                    break
    except Exception as e:
        print(e)


# Selection sort algorithm
def SelectionSort(a):
    try:
        for i in range(0, len(a) - 1):
            minIndex = i
            for j in range(i + 1, len(a)):
                if a[j] < a[minIndex]:
                    a[j], a[minIndex] = a[minIndex], a[j]
    except Exception as e:
        print(e)
   

# Bubble sort algorithm
def BubbleSort(a):
    try:
        for i in range(0, len(a) - 1):
            for j in range(0, len(a) - 1 - i):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
    except Exception as e:
        print(e)


# Merge sort algorithm
def MergeSort(a):
    try:
        SplitList(a, 0, len(a) - 1)
    except Exception as e:
        print(e)
    
def SplitList(a, first, last):
    try:
        if first < last:
            middle = (first + last)//2
            SplitList(a, first, middle)
            SplitList(a, middle + 1, last)
            MergeList(a, first, middle, last)
    except Exception as e:
        print(e)
        
def MergeList(a, first, middle, last):
    try:
        L = a[first:middle + 1]
        R = a[middle + 1:last + 1]
        L.append(sys.maxsize)
        R.append(sys.maxsize)
        i = j = 0
        for k in range(first, last + 1):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
    except Exception as e:
        print(e)

    


