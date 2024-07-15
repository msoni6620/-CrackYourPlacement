from collections import Counter
def sortColors(nums):
        m=nums.count(0)
        n=nums.count(1)
        j=nums.count(2)
        del nums[:]
        nums.extend([0]*m)
        nums.extend([1]*n)
        nums.extend([2]*j)
        return nums
        
n=list(map(int,input().split()))
print(sortColors(n))