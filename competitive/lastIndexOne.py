# Given a string S consisting only '0's and '1's,  find the last index of the '1' present in it.
# Example 1:

# Input:
# S = 00001
# Output:
# 4
# Explanation:
# Last index of  1 in given string is 4.
 

# Example 2:

# Input:
# 0
# Output:
# -1
# Explanation:
# Since, 1 is not present, so output is -1.

def lastIndex(s):
    for i in range(len(s)- 1, -1 , -1):
        if s[i] == '1':
            return i
    # Reached here means no one in the string
    return -1
        
# Time complexity : O(n)
s = '1000'
print(lastIndex(s))