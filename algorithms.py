import math
import numpy as np
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

def longest_common_subsequence(X,Y):
    m, n = len(X), len(Y)
    paths = [[i for i in range(m)] for j in range(n)]
    commons = [[i for i in range(m)] for j in range(n)]
    for i in range(1,m): 
        commons[i][0] = 0
    for j in range(n):
        commons[0][j] = 0
    for i in range(1,m):
        for j in range(1,n):
            if X[i] == Y[j]:
                commons[i][j] = commons[i-1][j-1] + 1
                paths[i][j] = 'up left'
            elif commons[i-1][j] >= commons[i][j-1]:
                commons[i][j] = commons[i-1][j]
                paths[i][j] = 'up'
            else:
                commons[i][j] = commons[i][j-1]
                paths[i][j] = 'left'
    return commons, paths

def print_LCS(paths,X,i,j,lcs):
    if i==0 or j==0:
        return
    if paths[i][j] == 'up left':
        print_LCS(paths,X,i-1,j-1,lcs)
        print(X[i])
        lcs.append(X[i])
    elif paths[i][j] == 'up':
        print_LCS(paths,X,i-1,j,lcs)
    else:
        print_LCS(paths,X,i,j-1,lcs)
    return lcs

def run_LCS():
    dna = {0:'a', 1:'c', 2:'g', 3:'t'}
    X = [dna[np.random.randint(4)] for i in range(20)]
    Y = [dna[np.random.randint(4)] for i in range(20)]
    commons, path = longest_common_subsequence(X,Y)
    lcs = []
    lcs = print_LCS(path,X,len(X)-1,len(Y)-1,lcs)

def optimal_BST(p,q,n):
    """
    >>> ex = [np.random.randint(100) for i in range(10)]
    >>> rootoo = [np.random.randint(100) for i in range(10)]
    >>> ex, rootoo = optimal_BST(ex, rootoo, 10)
    >>> print(np.array(ex))
    >>> print(np.array(rootoo))
    """
    e = [[i for i in range(1,n+1)] for j in range(n)]
    w = [[i for i in range(1,n+1)] for j in range(n)]
    root = [[i for i in range(1,n)] for j in range(1,n)]
    for i in range(1,n):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    for l in range(1,n):
        for i in range(1,n-l+1):
            j = i+l-1
            e[i][j] = math.inf
            w[i][j] = w[i][j-1] + p[j] + q[j]
            for r in range(i,j):
                t = e[i][r-1] + e[r+1][j] + w[i][j]
                if t < e[i][j]:
                       e[i][j] = t
                    root[i][j] = r
  
    return e, root
