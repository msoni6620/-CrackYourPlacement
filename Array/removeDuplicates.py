
from collections import Counter


def removeDuplicates(nums):
        c=Counter(nums)

        j=0
        for i in c.keys():
            nums[j]=i
            j+=1
        del nums[j:]
        nums.sort()
        return len(nums)
n=list(map(int,input().split()))
print(removeDuplicates(n))