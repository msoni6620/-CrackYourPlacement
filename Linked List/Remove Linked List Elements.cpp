
class Solution {
public:
    void push(ListNode *&head,int d)
    {
        ListNode *newn=new ListNode(d);
        newn->next=head;
        head=newn;
    }
    ListNode* rev(ListNode *head)
    {
        ListNode *prev=NULL;
        ListNode* curr=head;
        while(curr!=NULL)
        {
            ListNode* forw=curr->next;
            curr->next=prev;
            prev=curr;
            curr=forw;
        }
        return prev;
    }
    ListNode* removeElements(ListNode* head, int t) {
        if(head==NULL)
        {
            return head;
        }
        ListNode* curr=NULL;
        ListNode *temp=head;
        while(temp!=NULL)
        {
            if(temp->val==t){
                temp=temp->next;
                continue;
            }
            else{
                push(curr,temp->val);
                temp=temp->next;
            }
        }
        curr=rev(curr);
        return curr;
    }
};