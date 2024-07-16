class Solution(object):
    def maxArea(self, height):
        ans=float('-inf')
        i=0
        j=len(height)-1
        while(i<j):
            dis=j-i
            if(height[j]>height[i]):
                ans=max(ans,dis*height[i])
                i+=1
            else:
                ans=max(ans,dis*height[j])
                j-=1
        return ans 
                
