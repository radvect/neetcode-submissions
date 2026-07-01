class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_mins = [2**31]

    def push(self, val: int) -> None:
            
        self.stack_mins.append(min(self.stack_mins[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_mins[-1]
        
