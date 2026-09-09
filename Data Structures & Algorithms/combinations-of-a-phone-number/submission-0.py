class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        if not digits:
            return res

        def backtrack(res, curr, i):

            if i == len(digits):
                res.append(curr)
                return

            for ch in digit_map[digits[i]]:
                backtrack(res, curr + ch, i + 1)

        backtrack(res, "", 0)

        return res
        

            



