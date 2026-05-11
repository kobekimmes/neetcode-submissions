class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False
        
        alphabet = [0] * 26

        for ch in s1:
            alphabet[ord(ch) - 97] = alphabet[ord(ch) - 97]+1

        l, r = 0, len(s1)
        
        while r <= len(s2):
            print(alphabet)
            i = l
            while i < r and alphabet[ord(s2[i]) - 97] > 0:
                alphabet[ord(s2[i]) - 97] = alphabet[ord(s2[i]) - 97]-1
                i+=1
            print(alphabet)

            if (i - l) == len(s1):
                return True

            alphabet = [0] * 26
            for ch in s1:
                alphabet[ord(ch) - 97] = alphabet[ord(ch) - 97]+1

            r += 1
            l += 1
        
        return False


