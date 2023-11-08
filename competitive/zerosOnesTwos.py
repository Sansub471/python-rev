# A given array has only zeros, ones, and twos
# Arrange them in ascending order

def zeroOneTwo(arr, n):
    if len(arr) <= 1:
        return arr
    zeros = []
    ones = []
    twos = []
    for elem in arr:
        if elem == 0:
            zeros.append(elem)
        elif elem == 1:
            ones.append(elem)
        else:
            twos.append(elem)
    zeros.extend(ones)
    zeros.extend(twos)
    return zeros

# After tips
def zerosOnesTwos(arr, n):     
    low=0
    high=n-1
    mid=0
        
    #iterating until mid pointer is less than or equal to high.
    while mid<=high:
            
        #if element at mid is 0, swap with element at low and move both pointers.
        if arr[mid]== 0:
            arr[mid] , arr[low] = arr[low] , arr[mid]
            mid+=1
            low+=1
                
        #if element at mid is 1, move mid pointer.
        elif arr[mid]== 1:
            mid+=1
                
        #if element at mid is 2, swap with element at high and move high pointer.
        else:
            arr[mid] , arr[high] = arr[high] , arr[mid]
            high-=1
    return arr


arr = [0,2,1,2,0]
n = len(arr)
print(zeroOneTwo(arr, n))

print("This is the code after hint : ")
print(zerosOnesTwos(arr, n))

# This looks easy but not a easy one to do.