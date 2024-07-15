from itertools import permutations
def uniquePerms(arr, n):
        s=permutations(arr)
        l=list(set(s))
        return sorted(l)
arr=list(map(int,input().split()))
n=int(input())
print(uniquePerms(arr,n))