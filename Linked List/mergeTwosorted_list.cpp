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
    void solve(ListNode* &head,int data)
    {
        ListNode* newnode=new ListNode(data);
        newnode->next=head;
        head=newnode;
    }
    ListNode* reverse(ListNode *head)
    {
        ListNode* curr=head;
        ListNode* prev=NULL;
        while(curr!=NULL)
        {
            ListNode* fore=curr->next;
            curr->next=prev;
            prev=curr;
            curr=fore;
        }
        return prev;
    }
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1==NULL)
        {
            return list2;
        }
        if(list2==NULL)
        {
            return list1;
        }
        vector<int> ans;
        ListNode* temp=list1;
        while(temp!=NULL)
        {
            ans.push_back(temp->val);
            temp=temp->next;
        }
        ListNode* temp2=list2;
        while(temp2!=NULL)
        {
            ans.push_back(temp2->val);
            temp2=temp2->next;
        }
        sort(ans.begin(),ans.end());
        ListNode *curr=NULL;
        for(int i=0;i<ans.size();i++)
        {
            solve(curr,ans[i]);
        }
        curr=reverse(curr);
        return curr;
    }
};