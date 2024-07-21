#User function Template for python3
import  numpy  as np
class Solution:
    def productExceptSelf(self, nums, n):
        l=[1]*n
        left_prod=1
        for i in range(n):
            l[i]=left_prod
            left_prod*=nums[i]
        right_prod=1
        for i in range(n-1,-1,-1):
            l[i]*=right_prod
            right_prod*=nums[i]
        return l