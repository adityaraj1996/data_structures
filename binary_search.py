'''
In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop,
is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value
to the middle element of the array.
Worst complexity: O(log n)
Average complexity: O(log n)
Best complexity: O(1)
'''

def binary_search(nums,x, l, r):
    if r >= l:
        mid = l + (r-l) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] > x:
            return binary_search(nums,x,l,mid-1)
        elif nums[mid] < x:
            return binary_search(nums, x, mid + 1, r)

    else:
        return -1


nums = [2, 3, 4, 10, 40]; x = 10
print(binary_search(nums, x, 0, len(nums)-1))