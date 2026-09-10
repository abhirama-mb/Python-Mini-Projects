


def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)

def partition(a, left, right):
    p = a[left]
    i = left + 1
    j = right

    while True:
        while i<=j and a[i] < p:  
            i += 1  # i stops at an element >= pivot 

        while i<=j and a[j] > p:  
            j -= 1  # j stops at an element <= pivot 

        if i > j:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[left], a[j] = a[j], a[left]
    return j


a = [100,20,50,120,10,30,20]
last_index = len(a) - 1
print(f'Before Sorting : {a}')
quick_sort(a, 0, last_index)
print(f'After Sorting : {a}')



"""
Quick Sort

Algorithm:  
    1. Choose the first element as the pivot.
    2. Use two pointers:
        - i moves from the left until it finds an element >= pivot.
        - j moves from the right until it finds an element <= pivot.
    3. Swap these elements while i <= j.
    4. When i > j, place the pivot at index j.
    5. Recursively quick sort the left and right partitions.

Time Complexity:
    - Best: O(n log n)
    - Average: O(n log n)
    - Worst: O(n²)

Space Complexity:
    - Average: O(log n) recursion stack
    - Worst: O(n) recursion stack

Properties:
    - Stable: No
    - Adaptive: No
    - In-place: Yes
    - Comparison-based: Yes
    - Divide and Conquer: Yes

"""