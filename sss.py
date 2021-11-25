import sys

def maxSum(arr,n,k):
        win_sum = sum(arr[:k])
        max_sum = win_sum
        for i in range(n-k):
                win_sum = win_sum - arr[i] + arr[i+k]
                max_sum = max(max_sum, win_sum)
        return max_sum

arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
