#User function Template for python3

'''
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

'''
class Solution:
    def solve(self,head,data):
        newNode=Node(data)
        if(head is None):
            head=newNode
        else:
            newNode.next=head
            head=newNode
        return head
    def compute(self,head):
        l=[]
        t=head
        while(t!=None):
            l.append(t.data)
            t=t.next
        l=l[::-1]
        k=l[0]
        m=[]
        m.append(k)
        for i in range(1,len(l)):
            if(l[i]>=k):
                k=l[i]
                m.append(k)
        del l[:]
        # m=m[::-1]
        c=None
        for i in m:
            c=self.solve(c,i)
        del m[::]
        return c