class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        l=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if(nums[i]+nums[j]+nums[k]==0):
                    if([nums[i],nums[j],nums[k]] not in l):
                        l.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif((nums[i]+nums[j]+nums[k])>0):
                    k-=1
                else:j+=1
        return l