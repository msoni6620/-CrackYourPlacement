class Solution(object):
    def subarraysDivByK(self, nums, k):
        d=[0]*k
        d[0]=1
        s=0
        cnt=0
        for i in nums:
            s+=i
            s=s%k
            cnt+=d[s]
            d[s]+=1
        return cnt

    