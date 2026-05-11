class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for exp in tokens:
            match exp:
                case "+":
                    num1 = stack.pop(0)
                    num2 = stack.pop(0)
                    stack = [num2 + num1] + stack
                case "-":
                    num1 = stack.pop(0)
                    num2 = stack.pop(0)
                    stack = [num2 - num1] + stack
                case "/":
                    num1 = stack.pop(0)
                    num2 = stack.pop(0)
                    stack = [int(float(num2)/num1)] + stack
                case "*":
                    num1 = stack.pop(0)
                    num2 = stack.pop(0)
                    stack = [num2 * num1] + stack
                case _:
                    stack = [int(exp)] + stack
        return stack[0]

