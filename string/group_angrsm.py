class Solution(object):
    def groupAnagrams(self, strs):
        d=dict()
        m=list(strs)
        
        for i in range(len(strs)):
            strs[i]="".join(sorted(strs[i]))
      
       
        for i in range(len(strs)):
            if(strs[i] in d):
                d[(strs[i])]=d[(strs[i])]+[i]
            else:
                d[strs[i]]=[i]
        l=[]
        for i in d.values():
            l.append(i)
        k=0
        
        for i in l:
      
            for j in range(len(i)):
                io=l[k][j]
            
                l[k][j]=m[io]
            k+=1
        return l
        