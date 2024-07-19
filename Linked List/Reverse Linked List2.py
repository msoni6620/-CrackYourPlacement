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
    def reverseBetween(self, head, left, right):
        l=[]
        temp=head
        while(temp!=None):
            l.append(temp.val)
            temp=temp.next
       
        i=left-1
        j=right-1
        while(i<=j):
            l[i],l[j]=l[j],l[i]
            i+=1
            j-=1
        l=l[::-1]
        l1=None
        for i in l:
            l1=self.solve(l1,i)
        return l1