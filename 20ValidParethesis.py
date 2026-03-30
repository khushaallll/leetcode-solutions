class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, f):
        self.stack.append(f)
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop()
        else:
            return None

def isValid(s: str) -> bool:
    p_stack = Stack()

    for le in s:
        if le == '(' or le == '{' or le == '[':
            p_stack.push(le)
        else:
            if le == ')' and p_stack.peek() != '(':
                return False
            elif le == ']' and p_stack.peek() != '[':
                return False
            elif le == '}' and p_stack.peek() != '{':
                return False
            else:
                p_stack.pop()
    if len(p_stack.stack) != 0:
        return False
    else:
        return True 

s1 = "["
s2 = "([)]"
print(isValid(s1))
print(isValid(s2))