def binarySearch(array, target):
    l = 0
    r = len(array) -1 

    while l <= r:

        mid = l + (r - l)// 2
        
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
            
    return -1


x = [0,1,21,33,45,45,61,71,72,73]
target = 33
print("The output is:",binarySearch(x,target))
