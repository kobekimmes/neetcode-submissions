class Solution:
    def longestPalindrome(self, s: str) -> str:

        # attempt 1. outward search from each position

        # strategy: from each character, perform an outward palindromic check,
        # and maintain a variable for the longest one seen

        def substring_pal(s, i, even=False):
            curr = "" if even else s[i] 
            l = i if even else i - 1 
            j = i + 1
            while l >= 0 and j < n and s[l] == s[j]:
                curr = s[l] + curr + s[j]

                l -= 1
                j += 1
            
            return curr, len(curr)


        n = len(s)
        res = ""
        longest = 0   

        for i in range(n):
            
            odd_pal, opl = substring_pal(s, i)
            even_pal, epl = substring_pal(s, i, True)


            if opl > longest:
                longest = opl
                res = odd_pal

            if epl > longest:
                longest = epl
                res = even_pal
        
        return res


        