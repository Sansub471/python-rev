
def subArray(arr, N, K):
    sub_num = N // K
    start = 0
    for i in range(sub_num):
        sub_arr = arr[start:(i+1)*K]
        arr[start:(i+1)*K] = sub_arr[-1::-1]
        start += K
    sub_arr = arr[start:]
    arr[start:] = sub_arr[-1::-1]
    return arr

arr = [1,2,3,4,5]
N = len(arr)
K = 3
print("This is my implementation : ")
print(subArray(arr, N, K))
print("\n")


# Given algorithm
# l = 1, r = min(n, k) for case when n < k
# while (l <= n) {
# reverseArray(l:r)
# l += k
# r = min(n, r + k)
# }
# arr = a1, a2, a3 ... , ak-1, ak, ak+1, ..., a2k, a2k+1, ... , a3k, ... , an-1, an
# a1 - ak first sub-array
# ak+1 - a2k second sub array and so on
# some elements might be left, less than k elements

def subArrayReverse(arr, N, K):
    l = 0
    r = min(N, K)
    while( l <= N):
        sub_arr = arr[l:r]
        arr[l:r] = sub_arr[-1::-1]
        l += K
        r = min(N, r + K)
    return arr

print("The array is : ", arr)
print("This is given code : ")
print(subArrayReverse(arr, N, K))
print("\n")
