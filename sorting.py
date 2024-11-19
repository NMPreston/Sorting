# Noah Preston, CSC-231-001

def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly swaps adjacent items that are in the wrong order
    
    1. Is your implementation in-place or not?
    Yes, this implementation is in-place 
    2. When would you use this sorting algorithm and when not?
    When you need a simple sorting algorithm for small data sets
    Don't use for big data sets since it will have a bad time complexity 
    """
    n = len(arr)  # Get the length of the array
    for i in range(n): # Iterate through each element in array
        for j in range(n - i - 1): # Iterate through array to last unsorted item
            if arr[j] > arr[j + 1]: # Check if item is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Swap items 
    return arr # Return array

def selection_sort(arr):
    """
    Selection Sort: Finds the min item and swaps with first unsorted item
    
    1. Is your implementation in-place or not?
    Yes, this implementation is in-place
    2. When would you use this sorting algorithm and when not?
    When using for small data sets
    Don't use for big data sets since it will have a bad time complexity 
    """
    n = len(arr) # Get the length of the array
    for i in range(n): # Iterate through each element in array
        min_idx = i # Current index is minimum 
        for j in range(i + 1, n): # # Iterate through array 
            if arr[j] < arr[min_idx]: 
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr # Return array

def insertion_sort(arr):
    """
    Insertion Sort: Inserts each item into its correct position 
    
    1. Is your implementation in-place or not?
    Yes, this implementation is in-place
    2. When would you use this sorting algorithm and when not?
    Used for small or nearly sorted data sets
    Don't use for big data sets since it will have a bad time complexity 
    """
    for i in range(1, len(arr)): # Start from index 
        key = arr[i] # Store current item
        j = i - 1 # Set position
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr # Return array 

def merge_sort(arr):
    """
    Merge Sort: Divides array into halves and sorts them back together
    
    1. Is your implementation in-place or not?
    No, this implementation is not in-place
    2. When would you use this sorting algorithm and when not?
    Large data sets, good time complexity 
    Don't use if memory storage is a problem 
    """
    if len(arr) > 1: # Base case 
        mid = len(arr) // 2 # Find middle
        left = arr[:mid] # Split array left half
        right = arr[mid:] # Split array right half

        merge_sort(left) # Sort left half
        merge_sort(right) # Sort right half

# Sort through array, searching left and right 

        i = j = k = 0 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left): 
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr # Return array

def quicksort(arr):
    """
    Quicksort: Partitions and quickly sorts
    
    1. Is your implementation in-place or not?
    No, this implementation is not in-place 
    2. When would you use this sorting algorithm and when not?
    Large data sets for good time complexity 
    Don't use if data set is too large and not enough memory storage 
    """
    if len(arr) <= 1: # Base case
        return arr # Return array
    pivot = arr[0] # First item for pivot 
    # left and right side for items less than and greater than pivot 
    left = [x for x in arr[1:] if x <= pivot] 
    right = [x for x in arr[1:] if x > pivot]
    return quicksort(left) + [pivot] + quicksort(right) # Return array

if __name__ == "__main__":
    example_list = [58, 27, 11, 4, 34, 65, 99]

    print("Original List:", example_list)
    print("Bubble Sort Result:", bubble_sort(example_list.copy()))
    print("Selection Sort Result:", selection_sort(example_list.copy()))
    print("Insertion Sort Result:", insertion_sort(example_list.copy()))
    print("Merge Sort Result:", merge_sort(example_list.copy()))
    print("Quicksort Result:", quicksort(example_list.copy()))

    print("\nBubble Sort Docstring:", bubble_sort.__doc__)
    print("\nSelection Sort Docstring:", selection_sort.__doc__)
    print("\nInsertion Sort Docstring:", insertion_sort.__doc__)
    print("\nMerge Sort Docstring:", merge_sort.__doc__)
    print("\nQuicksort Docstring:", quicksort.__doc__)