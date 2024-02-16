from icecream import ic 

def isValid(s):
    stack = []
    d = {'(':')', '{':'}', '[':']'}

    for p in s: 
        if p in d: # if left bracket, we append it
            stack.append(p)
            print(stack)
        # if right bracket and stack empty, pop it (as no match left)
        elif len(stack) == 0 or d[stack.pop()] != p:
            print(stack)
            return False
        ic(stack)
    
    return len(stack) == 0

    




# ic(isValid("()[]{}"))
ic(isValid("([]{})"))
# ic(isValid(")([]{})"))
# ic(isValid("()"))
# ic(isValid("(]"))
# ic(isValid(")("))