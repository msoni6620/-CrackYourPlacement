# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def solve(self,head,d):
        newNode=ListNode(d)
        if(head is None):
            head=newNode
        else:
            newNode.next=head
            head=newNode
        return head

    def removeNthFromEnd(self, head, n):
        c=0
        temp=head
        while(temp!=None):
            c+=1 
            temp=temp.next
        d=c-n+1
        t1=head
        t2=None
        l=[]
        if(d==1):
            return head.next
        else:
            p=None
            m=0
            while(t1!=None and m<d-1):
                m+=1
                p=t1
                l.append(t1.val)
                t1=t1.next
            t1=p
            t1=t1.next.next
            while(t1!=None):
                l.append(t1.val)
                t1=t1.next
        l=l[::-1]
        for i in l:
            t2=self.solve(t2,i)
        return t2