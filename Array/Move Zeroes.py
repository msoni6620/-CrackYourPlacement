def moveZeroes(nums):
        c=nums.count(0)
        l=[]
        for i in range(len(nums)):
            if(nums[i]!=0):
                l.append(nums[i])
        l.extend([0]*c)
        for i in range(len(nums)):
            nums[i]=l[i]
        return nums
print(moveZeroes([1,0,3,0,5]))
        