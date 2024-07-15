from collections import Counter
def findDuplicates(nums):
        c=Counter(nums)
        j=0
        for key,value in c.items():
            if(value>=2):
                nums[j]=key
                j+=1
        del nums[j:]
        return nums
nums=list(map(int,input().split()))
print(findDuplicates(nums))