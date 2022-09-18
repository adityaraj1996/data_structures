"""
Name: merge_sort.py
Author: Aditya Raj
Contact: aditya.raj@gartner.com
Time: 9/18/2022 3:08 PM
"""


"""
The Merge Sort algorithm is a sorting algorithm that is based on the Divide and Conquer paradigm.
 In this algorithm, the array is initially divided into two equal halves and then they are 
 combined in a sorted manner.
"""

#Time complexity ==> O(nlogn)

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

arr = [2, 3, 5, 1, 7, 4, 4, 0, 2, 3]
print(mergeSort(arr))
