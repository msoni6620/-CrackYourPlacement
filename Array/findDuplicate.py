from collections import Counter
def findDuplicate(nums):
        c=Counter(nums)
        for key,value in c.items():
            if(value>=2):
                return key
n=list(map(int,input().split()))
print(findDuplicate(n))
            