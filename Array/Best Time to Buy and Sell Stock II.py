def maxProfit(self, arr):
        maxi=0
        price=arr[0]
        for i in range(len(arr)):
            if(price<arr[i]):
                maxi+=(arr[i]-price)
            price=arr[i]
            
        return maxi

arr = [7, 1, 5, 3, 6, 4]
print(maxProfit(arr))
