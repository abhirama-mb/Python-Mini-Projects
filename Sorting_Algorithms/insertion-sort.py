def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key



a = [100,20,50,120,10,30,20]
print(f'Before Sorting : {a}')
insertion_sort(a)
print(f'After Sorting : {a}')

''' 
    Take each element and insert it into its correct position
    within the already sorted portion.

    Time Complexity: O(n²) | Best Case: O(n) | Space Complexity: O(1)

    Stable ✅ → equal elements maintain their relative order.
    Adaptive ✅ → performs faster on already/nearly sorted data.
    In-place ✅ → uses O(1) extra space.
'''