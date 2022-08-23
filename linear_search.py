'''
In computer science, a linear search or sequential search is a method for finding an element within a list. It sequentially checks each element of the list until a match is found or the whole list has been searched. Wikipedia
Worst complexity: O(n)
Average complexity: O(n)
Space complexity: O(1)
'''

def linear_search(nums,x):
    for i in range(len(nums)):
        if nums[i] == x:
            return(f"element {x} found at {i} index ")
    return (f"element {x} not found ")





nums = [2, 3, 4, 10, 40]; x = 100

print(linear_search(nums, x))
