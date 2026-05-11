class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def rec(s):
            if len(s) <= 1:
                return True
            if not s[0].isalnum():
                return rec(s[1:])
            if not s[-1].isalnum():
                return rec(s[:-1])
            if s[0].lower() == s[-1].lower():
                return rec(s[1:-1])
            return False
            
        return rec(s)
