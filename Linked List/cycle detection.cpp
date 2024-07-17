/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *temp=head;
        ListNode *fast=head;
        ListNode *prev=head;
        while(fast!=NULL &&fast->next!=NULL && prev!=NULL)
        {   
        fast=fast->next->next;
        prev=prev->next;
        if(fast==prev)
        {
            return true;
        }
            
        }
        return 0;
    }
};