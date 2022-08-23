'''
Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the
list, compares adjacent elements and swaps them if they are in the wrong order. The pass through the list is repeated
until the list is sorted.

Worst complexity: n^2
Average complexity: n^2
'''

def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        # # Last i elements are already in place
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))