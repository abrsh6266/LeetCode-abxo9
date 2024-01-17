class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        return len(self.items)
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(':1,
            ')':1,
            '[':2,
            ']':2,
            '{':3,
            '}':3,
        }
        stack = Stack()
        n = len(s)
        for i in range(n):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.push(s[i])
            else:
                if stack.is_empty():
                    return False
                else:
                    if dic[stack.peek()] == dic[s[i]]:
                        stack.pop()
                    else:
                        return False
        return stack.is_empty()
solution = Solution()
print(solution.isValid('()') )