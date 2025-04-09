def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90, 34, 65, 897, 98, 10, 23, 84, 63, 81, 90, 67, 23, 98, 10, 23, 84, 63, 81, 90, 67, 23]
sorted_numbers = selection_sort(numbers)
print("Sorted array:", sorted_numbers)