class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # attempt 1. brute force -- TLE (35/47)

        # strategy: for every word in strs, loops over every other
        # word in strs, and check if they are anagrams, if they are
        # add to array, otherwise skip

        def is_anagram(s1, s2):
            n, m = len(s1), len(s2)

            if n != m:
                return False

            s1_map, s2_map = char_map(s1), char_map(s2)

            for i in range(26):
                if s1_map[i] != s2_map[i]:
                    return False

            return True


        def char_map(s):
            s_map = [0] * 26
            for i in range(len(s)):
                s_map[97 - ord(s[i])] += 1
            return s_map

        
        def attempt1():
            n = len(strs)
            result = []
            grouped = set()
            for i in range(n):
                if i not in grouped:
                    s1 = strs[i]
                    group = [s1]
                    for j in range(n):
                        s2 = strs[j]
                        if i != j and j not in grouped:
                            if is_anagram(s1, s2):
                                group.append(s2)
                                grouped.add(j)
                    grouped.add(i)
                    result.append(group)

            return result

        # return attempt1()

        # attempt 2. decrease scan, o(n^2) -> o(n)
        
        # strategy: use a hashtable mapping a character
        # mapping of the string to the group of anagrams

        def attempt2():

            anagram_map = {}
            for s in strs:
                s_char_map_key = tuple(char_map(s))

                if s_char_map_key in anagram_map:
                    anagram_map[s_char_map_key].append(s)
                else:
                    anagram_map[s_char_map_key] = [s]

            return [group for group in anagram_map.values()]
        
        return attempt2()






                    




