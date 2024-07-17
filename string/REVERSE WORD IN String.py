class Solution(object):
    def reverseWords(self, s):
        l1=s.split()
        return " ".join(l1[::-1])