def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):

            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True

        if not swapped:
           return
            


a = [100,20,50,120,10,30,20]
print(f'Before Sorting : {a}')
bubble_sort(a)
print(f'After Sorting : {a}')



''' 
    Compare adjacent elements, swap if they're in the wrong order,
    and repeat until the largest remaining element bubbles to the end.   

    Time Complexity: O(n²) | Best Case: O(n) | Space Complexity: O(1)

    Stable ✅ → equal elements maintain relative order
    Adaptive ✅ → performs faster on already/nearly sorted data
    In-place ✅ → uses O(1) extra space
'''