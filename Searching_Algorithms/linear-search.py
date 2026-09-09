def linear_search(arr,target):
    for i,n in enumerate(arr):
        if n == target:
            return i
        
    return -1   # None


a = [100,20,50,120,10,30,20]
print(linear_search(a,10))    # 4
print(linear_search(a,2000))  # -1
