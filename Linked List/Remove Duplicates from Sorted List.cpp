/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==NULL)
        {
            return head;
        }
        ListNode *curr=head;
        while(curr!=NULL and curr->next!=NULL)
        {
            if(curr->val!=curr->next->val)
            {
                curr=curr->next;
            }
            else{
                ListNode *nextoto=curr->next->next;
                delete(curr->next);
                curr->next=nextoto;
            }
        }
        return head;
        
    }
};