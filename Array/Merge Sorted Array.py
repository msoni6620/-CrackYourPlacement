def merge(nums1, m, nums2, n):
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort()

nums1=list(map(int,input().split()))
m=int(input())
nums2=list(map(int,input().split()))
n=int(input())
print(merge(nums1,m,nums2,n))