class Solution(object):
    def longestCommonPrefix(self, strs):
        l=[]
        for i in strs:
            l.append(len(i))
        a=min(l)
        s=l.index(a)
        m=strs[s]
        print(m)
        o=''
        c=0
        for i in range(len(m)):
            for j in range(len(strs)):
                if(strs[j][i]!=m[i]):
                    c=1
                    break
            if(c==1):
                break
            else:
                o+=m[i]
        return o



        