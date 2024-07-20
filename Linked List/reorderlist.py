# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addi(self,head,d):
        newN=ListNode(d)
        if(head is None):
            head=newN
        else:
            newN.next=head
            head=newN
        return head
    def reorderList(self, head: Optional[ListNode]) -> None:
        c=0
        t=head
        l=[]
        while(t!=None):
            c+=1
            l.append(t.val)
            t=t.next
        m=l[:len(l)//2]
        n=l[len(l)//2:][::-1]
        k=[]
        i=0
        j=0
        while(i<len(m) and j<len(n)):
            k.append(m[i])
            k.append(n[j])
            i+=1
            j+=1
        while(i<len(m)):
            k.append(m[i])
            i+=1
        while(j<len(n)):
            k.append(n[j])
            j+=1
        curr=None
        for i in k[::-1]:
            curr=self.addi(curr,i)
        while(curr!=None):
            head.val=curr.val
            curr=curr.next
            head=head.next
        return head
        


    
        