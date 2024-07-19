# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def solve(self,head,d):
        l=ListNode(d)
        if(head is None):
            head=l
        else:
            l.next=head
            head=l
        return head
    def addTwoNumbers(self, l1, l2):
        s=''
        s2=''
        temp=l1
        temp2=l2
        while(temp!=None):
            s+=str(temp.val)
            temp=temp.next
        while(temp2!=None):
            s2+=str(temp2.val)
            temp2=temp2.next
        print(s,s2)
        s3=str(int(s)+int(s2))[::-1]

        l1=None
        for i in s3:
            l1=self.solve(l1,int(i))
        return l1
        