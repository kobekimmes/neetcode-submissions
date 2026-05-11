class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0

        cur_len = 0

        char_dict = {}

        while r < len(s):
            while char_dict.get(s[r], False) and l <= r:
                char_dict[s[l]] = False
                l+=1
                  
            cur_len = max(cur_len, r - l + 1)
            char_dict[s[r]] = True

            r+=1
        
        return cur_len
            
