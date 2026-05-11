class Solution:
    def isValid(self, s: str) -> bool:
        
        left = "{(["
        right = "})]"
        stack = []

        for ch in s:
            if ch in left:
                stack = [ch] + stack
            else:
                if len(stack) == 0: return False
                cur = stack.pop(0)
                match ch:
                    case "}": 
                        if cur != "{":
                            return False
                    case ")":
                        if cur != "(":
                            return False
                    case "]":
                        if cur != "[":
                            return False

        return len(stack) == 0

                
