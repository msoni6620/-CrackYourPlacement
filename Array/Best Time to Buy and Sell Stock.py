def maxProfit(arr):
    mini = float('inf')
    maxi = 0
    for i in range(len(arr)):
        if arr[i] < mini:
            mini = arr[i]
        maxi = max(arr[i] - mini, maxi)
    return maxi

arr = [7, 1, 5, 3, 6, 4]
print(maxProfit(arr))