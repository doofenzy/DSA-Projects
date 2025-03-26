arr = [23, 65 ,87, 98, 10, 23, 84, 63, 81, 90]
arr.sort() # binary search only works when the data is sorted
target = 98

def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

print(binarySearch(arr, target))

# Time Complexity:
# Best Case: O(1)
# Average Case: O(log N)
# Worst Case: O(log N)