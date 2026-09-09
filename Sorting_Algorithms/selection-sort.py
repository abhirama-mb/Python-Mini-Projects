def selection_sort(arr):
    n = len(arr)

    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


a = [100,20,50,120,10,30,20]
print(f'Before Sorting : {a}')
selection_sort(a)
print(f'After Sorting : {a}')


''' 

    Find the minimum element from the unsorted portion and
    place it at the beginning of that portion.
     
    Time Complexity: O(n²) | Best Case: O(n²) | Space Complexity: O(1) 

    Stable ❌ → equal elements may change their relative order. 
    Adaptive ❌ → performance does not improve for sorted/nearly sorted data. 
    In-place ✅ → uses O(1) extra space. 
    
'''

