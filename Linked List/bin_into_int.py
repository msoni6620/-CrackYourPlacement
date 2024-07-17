
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp=head
        s=''
        while(temp!=None):
            s+=str(temp.val)
            temp=temp.next
        return int(s,2)
        