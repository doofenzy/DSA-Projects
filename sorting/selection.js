function selection_sort(arr, n){
    // Start with the whole array as unsorted and one by
  	// one move boundary of unsorted subarray towards right
    for(i = 0; i < n - 1; i++){
        // n - 1: The loop will iterate up to the second-to-last element of the array. 
        // This is because, in selection sort, the last element will already be in its 
        // correct position after sorting the rest of the array. There's no need to compare it further.

        // n: If you use n instead of n - 1, the loop will iterate through all elements, 
        // including the last one. This would result in unnecessary comparisons since the
        //  last element doesn't need to be checked after the previous iterations 

        // Find the minimum element in unsorted array
        min_index = i;
        for(j = i + 1; j < n; j++){
            if(arr[j] < arr[min_index]){
                min_index = j
            }
        }

        // Swap the found minimum element with the first
        // element in the unsorted par
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp;
    } 
    
    return arr
}

arr = [64, 25, 12, 22, 11]
n = arr.length
console.log("Unsorted array: " + arr)
console.log("Sorted array: " + selection_sort(arr, n))



