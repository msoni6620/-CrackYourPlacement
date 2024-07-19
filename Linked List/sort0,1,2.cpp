class Solution

{   public:
    void solve(Node* &head,int data)
    {
        Node* newnode=new Node(data);
        newnode->next=head;
        head=newnode;
    }
    Node* reverse(Node *head)
    {
        Node* curr=head;
        Node* prev=NULL;
        while(curr!=NULL)
        {
            Node* fore=curr->next;
            curr->next=prev;
            prev=curr;
            curr=fore;
        }
        return prev;
    }
    public:
    //Function to sort a linked list of 0s, 1s and 2s.
    Node* segregate(Node *head) {
        vector<int> ans;
        Node*temp=head;
        while(temp!=NULL)
        {
            ans.push_back(temp->data);
            temp=temp->next;
            
            
        }
        sort(ans.begin(),ans.end());
        Node *curr=NULL;
        for(int i=0;i<ans.size();i++)
        {
            solve(curr,ans[i]);
        }
        curr=reverse(curr);
        return curr;
        
    }
};
