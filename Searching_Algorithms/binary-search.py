def binary_search(arr,target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        cur = arr[mid]

        if cur == target:
            return mid
        
        if cur > target:
            right = mid -1
        else:
            left = mid + 1

    return -1

# to apply Binary search, arr must be sorted

a = [10,20,30,40,50,60,100,400] 
print(binary_search(a,60))    # 5
print(binary_search(a,2000))  # -1

# log n

