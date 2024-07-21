#User function Template for python3

class Solution:
    def solve(self,head,data):
        newNode=Node(data)
        if(head is None):
            head=newNode
        else:
            newNode.next=head
            head=newNode
        return head
    def subLinkedList(self, l1, l2): 
        s=''
        s1=''
        t=l1
        t2=l2
        while(t!=None):
            s+=str(t.data)
            t=t.next
        while(t2!=None):
            s1+=str(t2.data)
            t2=t2.next
        s3=''
        if(int(s)>int(s1)):
            s3=str(int(s)-int(s1))[::-1]
        else:
            s3=str(int(s1)-int(s))[::-1]
        ne=None
        for i in s3:
            ne=self.solve(ne,int(i))
        return ne

