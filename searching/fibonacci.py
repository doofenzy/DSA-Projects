def fibonacciSearch(arr, target):
    n = len(arr)
    fib2, fib1 = 0, 1
    fib = fib1 + fib2
    while fib < n:
        fib2, fib1 = fib1, fib
        fib = fib1 + fib2

    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if arr[i] < target:
            fib, fib1, fib2 = fib1, fib2, fib - fib1
            offset = i
        elif arr[i] > target:
            fib, fib1, fib2 = fib2, fib1 - fib2, fib - fib1
        else:
            return i
    return None


arr = [23, 65 ,87, 98, 10, 23, 84, 63, 81, 90]
arr.sort() # binary search only works when the data is sorted
target = 98
print(fibonacciSearch(arr, target))

# time complexity: O(logn)