import math
def insertion_sort(array, incrs=True):
    for j in range(1, len(array)):
        key = array[j]
        i = j-1
        if incrs:
            while i > -1 and array[i] > key:
                array[i+1] = array[i]
                i -= 1
        else:
            while i > -1 and array[i] < key:
                array[i+1] = array[i]
                i -= 1
        array[i+1] = key

def insertion_sort_decr(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j-1
        while i > -1 and array[i] < key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key

def mergesort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

def qsort_simple(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array

def qsort_inplace(array, low, high):
    if low < high:
        partition = qsort_partition(array, low, high)
        qsort_inplace(array, low, partition-1)
        qsort_inplace(array, partition+1, high)

def qsort_partition(array, low, high):
    pivot = array[high]
    begin = low - 1
    for end in range(low, high):
        if array[end] < pivot:
            begin += 1
            array[begin], array[end] = array[end], array[begin]
    if array[high] < array[begin + 1]:
        array[begin + 1], array[high] = array[high], array[begin + 1]
    return begin + 1
