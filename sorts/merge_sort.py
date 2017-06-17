"""
This is a pure python implementation of the merge sort algorithm

For manual testing run:
python merge_sort.py
"""
import sys

# 1st routine: split the input array recursively
# until atomic sub-arrays are reached
def mergeSort(inArray, first, last):
    if first < last:
        middle = (first + last) / 2          # returns floored int
        mergeSort(inArray, first, middle)
        mergeSort(inArray, middle + 1, last)
        merge(inArray, first, middle, last)

# 2nd routine: merge individual sub-arrays to one sorted array
def merge(inArray, first, middle, last):
    n1 = middle - first + 1 # length of inArray[first,middle]
    n2 = last - middle      # length of inArray[middle+1,last]

    leftArray = []
    rightArray = []
    for i in range(n1):
        leftArray.append(inArray[first+i])
    for j in range(n2):
        rightArray.append(inArray[middle+1+j])

    # maxint as the sentinel (last value) guarantees 
    # that both subarrays will be processed completely 
    leftArray.append(sys.maxint)
    rightArray.append(sys.maxint)

    i,j = 0,0
    k = first
    while k <= last:
        if leftArray[i] <= rightArray[j]:
            inArray[k] = leftArray[i]
            i += 1
        else:
            inArray[k] = rightArray[j]
            j += 1
        k += 1

# alternative merge implmementation, using
# python's arrays slicing utilities		
def merge2(inArray, first, middle, last):
    leftArray = inArray[first:middle+1]
    rightArray = inArray[middle+1:last+1]

    # maxint as the last value guarantees that both
    # subarrays will be processed completely
    leftArray.append(sys.maxint)
    rightArray.append(sys.maxint)

    i,j = 0,0
    k = first
    while k <= last:
        if leftArray[i] <= rightArray[j]:
            inArray[k] = leftArray[i]
            i += 1
        else:
            inArray[k] = rightArray[j]
            j += 1
        k += 1
		
