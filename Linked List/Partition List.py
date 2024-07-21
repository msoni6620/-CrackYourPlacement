# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def solve(self,head,data):
        newNode=ListNode(data)
        if(newNode is None):
            head=newNode
        else:
            newNode.next=head
            head=newNode
        return head
    def rev(self,head):
        prev=None
        curr=head
        while(curr!=None):
            forw=curr.next
            curr.next=prev
            prev=curr
            curr=forw
        return prev
    def partition(self, head, x):
        c=head
        c1=None
        while(c!=None):
            if(c.val<x):
                c1=self.solve(c1,c.val)
            c=c.next
        c=head
        while(c!=None):
            if(c.val>=x):
                c1=self.solve(c1,c.val)
            c=c.next
        c1=self.rev(c1)
        return c1
            
        
        