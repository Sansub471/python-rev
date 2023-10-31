# Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
# For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

# Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

# Example 1:

# Input:
# {([])}
# Output: 
# true
# Explanation: 
# { ( [ ] ) }. Same colored brackets can form 
# balanced pairs, with 0 number of 
# unbalanced bracket.
# Example 2:

# Input: 
# ()
# Output: 
# true
# Explanation: 
# (). Same bracket can form balanced pairs, 
# and here only 1 type of bracket is 
# present and in balanced way.
# Example 3:

# Input: 
# ([]
# Output: 
# false
# Explanation: 
# ([]. Here square bracket is balanced but 
# the small bracket is not balanced and 
# Hence , the output will be unbalanced.

# Solution using stack
def ispar(x):
    stack = []
    for char in x:
        #print(stack)
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        elif char == '}' or char == ']' or char == ')':
            if len(stack) == 0:
                return False
            else:
                p = stack[-1]
                if p == '(' and char == ')' or p == '{' and char == '}' or p == '[' and char == ']':
                    stack.pop()
                else:
                    return False
    return True if len(stack) == 0 else False

x = '(([{<A*(B+C)>}] - [{D/E}]) * {F[G] - H} / [I{J}])'
y = '(((({{[<A*(B+C)>]} - [{D/E}]} * {{F[G] - H}} / [I{J}]) + [K<[L*M]>]) - {{M[(N+O)]} * [P{Q}]}) / [R<S>])'
print(ispar(x))
print(ispar(y))
