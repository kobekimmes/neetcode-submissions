class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        n = len(s)

        t_dict = {}
        s_dict = {}

        for i in range(n):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            elif s[i] not in s_dict:
                s_dict[s[i]] = 1

            if t[i] in t_dict:
                t_dict[t[i]] += 1
            elif t[i] not in t_dict:
                t_dict[t[i]] = 1

        for i in range(n):
            if s_dict.get(s[i]) != t_dict.get(s[i]):
                return False
        
        return True





        