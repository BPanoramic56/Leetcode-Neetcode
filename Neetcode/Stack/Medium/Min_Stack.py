# Completed: 01/15/2026

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            current_min = self.min_stack[len(self.min_stack) - 1]
            if val < current_min:
                self.min_stack.append(val)
            else:
                self.min_stack.append(current_min)

    def pop(self) -> None:
        last_val = self.stack[-1]
        self.stack = self.stack[:len(self.stack) - 1]
        self.min_stack = self.min_stack[:len(self.min_stack) - 1]
        return last_val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]
        
