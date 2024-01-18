import sys
class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:        
        self.items.append(val)
    def pop(self) -> None:
        if len(self.items) != 0:
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")
    def top(self) -> int:
        if len(self.items) != 0:
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")
    def getMin(self) -> int:
        if len(self.items) != 0:
            return sorted(self.items)[0]
        else:
            raise IndexError("peek from an empty stack")


# Your MinStack object will be instantiated and called as such: