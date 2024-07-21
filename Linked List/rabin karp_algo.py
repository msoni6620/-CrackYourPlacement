#User function Template for python3

class Solution:
    def search(self, pattern, text):
        l=[]
        for i in range(len(text)):
            m=text.find(pattern,i)
            if(m==-1):
                break
            l.append(m+1)
    
            
        return sorted(list(set(l)))
            
