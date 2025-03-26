arr = [23, 65 ,87, 98, 10, 23, 84, 63, 81]
target = 87
def linearSearch(arr, target):
    index = 0
    for i in range(0, len(arr)):
        if arr[i] == target:
            index = i
            return index
    return -1

print(linearSearch(arr, target))

# Best Case: In the best case, the key might 
# be present at the first index. So the best case complexity is O(1)

# Worst Case: In the worst case, the key might be present at the last index i.e.,
#   opposite to the end from which the search has started in the list.
#   So the worst-case complexity is O(N) where N is the size of the list.

# Average Case: O(N)