
def subArray(arr, N, K):
    sub_num = N // K
    start = 0
    for i in range(K):
        sub_arr = arr[start:(i+1)*sub_num]
        arr[start:(i+1)*sub_num] = sub_arr[-1::-1]
        start += sub_num
    sub_arr = arr[start:]
    arr[start:] = sub_arr[-1::-1]
    return arr

arr = [1,2,3,4,5]
N = len(arr)
K = 3
print(subArray(arr, N, K))