def in_int(num: str) -> bool:
    try:
        n = int(num)
        return True
    except ValueError:
        return False
    

def evalRPN(tokens: list[str]) -> int:
    
    operations = {
        "+": lambda l,r: l+r,
        "-": lambda l,r: l-r,
        "/": lambda l,r: int(l/r),
        "*": lambda l,r: l*r
    }
    
    cal_stack = []
    for val in tokens:
        if val not in operations:
            cal_stack.append(int(val))
        else:
            right_operand = cal_stack.pop()
            left_operand = cal_stack.pop()
            current = operations[val](left_operand, right_operand)
            cal_stack.append(current)
    
    return cal_stack[0]


tokens = ["4","13","5","/","+"]
print("Final Answer: ",evalRPN(tokens))