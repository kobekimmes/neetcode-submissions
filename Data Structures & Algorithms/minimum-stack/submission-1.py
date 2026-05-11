class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 or self.min_stack[0] >= val:
            self.min_stack = [val] + self.min_stack
        
        self.stack = [val] + self.stack

    def pop(self) -> None:
        if self.stack[0] == self.min_stack[0]:
            self.min_stack = self.min_stack[1:]
            
        self.stack = self.stack[1:]

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min_stack[0]
        
