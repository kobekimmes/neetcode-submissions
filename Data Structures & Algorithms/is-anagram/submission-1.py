class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        hmap = [0] * 26

        i = 0
        n = len(s)
        while i < n:
            hmap[ord(s[i])-97] += 1
            hmap[ord(t[i])-97] -= 1
            i+=1   

        for val in hmap:
            if val != 0:
                return False
        return True

        

        
        




        