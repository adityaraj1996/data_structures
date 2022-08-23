'''
The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
 from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray
 is picked and moved to the sorted subarray.
 Worst complexity: n^2
'''

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min = i
        # traversing unsorted sub array to find the minimum element less than num[i]
        for j in range(i+1,n):
            if nums[min] > nums[j]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums

arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))


