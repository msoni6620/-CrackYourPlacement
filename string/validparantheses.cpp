#include<string>
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for(auto it:s){
            if(it=='(' || it=='{' || it=='[')
            {
                st.push(it);
            }
            else{
                if(st.empty())
                {
                    return 0;
                }
                
                char ch=st.top();
                st.pop();
                if((ch=='(' and it==')')||( ch=='{' and it=='}') || (ch=='[' and it==']'))
                {
                    continue;
                }
                else{
                    return 0;
                }

            }
        }
        return st.empty();
        
    }
};