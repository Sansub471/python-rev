# Given a string S consisting of lowercase Latin Letters. Return the first non-repeating character in S. 
# If there is no non-repeating character, return '$'.

# Example 1:

# Input:
# S = hello
# Output: h
# Explanation: In the given string, the
# first character which is non-repeating
# is h, as it appears first and there is
# no other 'h' in the string.
# Example 2:

# Input:
# S = zxvczbtxyzvy
# Output: c
# Explanation: In the given string, 'c' is
# the character which is non-repeating. 

# Find the first non repeating character in a string.
# Easy way is to create a nested loop

# Let's try the nested loop solution
def nonrepeatingCharacter(s):
    for i in range(0, len(s)):
        j = 0
        while(j < len(s)):
            if i == j:
                j += 1
                continue
            if s[i] == s[j]:
                break
            else:
                j += 1
        if j == len(s):
            return s[i]
    return '$'

s = 'yyx'
#s = 'hello'
print(nonrepeatingCharacter(s))