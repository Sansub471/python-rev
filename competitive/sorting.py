# Let's try a sorting technique from out of memory

arr = [20,9,3,2,1]
def sorting(arr):
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

print(sorting(arr))

# Time to go home, it's a bad day.