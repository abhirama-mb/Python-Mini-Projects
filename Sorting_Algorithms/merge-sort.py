

def merge_sort(arr,left,right):
    if len(arr) <= 1:
        return
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)

def merge(arr,left,mid,right):
    i = left
    j = mid + 1
    res = []

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i += 1
        else:
            res.append(arr[j])
            j += 1

    res.extend(arr[i : mid+1])
    res.extend(arr[j : right+1])

    arr[left : right+1] = res

a = [100,20,50,120,10,30,20]
last_index = len(a) - 1
print(f'Before Sorting : {a}')
merge_sort(a, 0, last_index)
print(f'After Sorting : {a}')

"""
Merge Sort

Algorithm:

1. Divide the array into two halves recursively until each part contains one element.

2. Merge the two sorted halves by comparing their elements and 
   storing them in a temporary list.

3. Copy the merged result back into the corresponding portion of the original array.

Time Complexity:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity:
- O(n) auxiliary space for the temporary merge list.

Properties:
- Stable: Yes
- Adaptive: No
- In-place: No
- Comparison-based: Yes
- Divide and Conquer: Yes
"""













