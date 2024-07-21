class Solution:
    def Anagrams(self, words, n):
        d=dict()
        for i in range(len(words)):
            if("".join(sorted(words[i])) in d):
                d["".join(sorted(words[i]))]=d["".join(sorted(words[i]))]+[i]
            else:
                d["".join(sorted(words[i]))]=[i]
       
        p=[]
        for key in d.values():
            p1=[]
            for i in key:
                p1.append(words[i])
            p.append(p1)
                
        return p

