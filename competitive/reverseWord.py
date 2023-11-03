# Given a String S, reverse the string without reversing its individual words. Words are separated by dots.

# Example 1:

# Input:
# S = i.like.this.program.very.much
# Output: much.very.program.this.like.i
# Explanation: After reversing the whole
# string(not individual words), the input
# string becomes
# much.very.program.this.like.i
# Example 2:

# Input:
# S = pqr.mno
# Output: mno.pqr
# Explanation: After reversing the whole
# string , the input string becomes
# mno.pqr


def reverseWords(S):
    # code here 
    new_S = ''
    temp = ''
    for char in S:
        if char == '.':
            new_S = char + temp + new_S
            temp = ''
        else:
            temp += char
    new_S = temp + new_S # For the last remaining word
    return new_S

S = 'pqr.mno'
S = 'i.like.this.program.very.much'
print(reverseWords(S))