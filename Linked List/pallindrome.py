# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        l=[]
        li=head
        while(li!=None):
            l.append(li.val)
            li=li.next
        return l==l[::-1]
        