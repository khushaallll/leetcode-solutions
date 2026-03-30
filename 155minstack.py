class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
            
    def top(self) -> int:
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def getMin(self) -> int:
        return self.min_stack[-1]

    def is_empty(self) -> bool:
        return len(self.stack) == 0

'''
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
'''

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_3 = obj.getMin()
print("get min: ",param_3)
obj.pop()
param_4 = obj.top()
print("Top ele: ",param_4)
param_5 = obj.getMin()
print("get min: ",param_5)