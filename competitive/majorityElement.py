# An element in an array is called majority element if it occurs strictly more than N/2 times
# N is the size of the array

# Input:
# N = 5 
# A[] = {3,1,3,3,2} 
# Output:
# 3
# Explanation:
# Since, 3 is present more
# than N/2 times, so it is 
# the majority element.

class Solution:
    # use linear search to compute candidate for majority element
    def findCandidate(self, A):
        maj_index = 0
        count = 1
        for i in range(len(A)):
            if A[maj_index] == A[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                maj_index = i
                count = 1
        return A[maj_index]
        
    # Function to check if the candidate occurs more than n/2 times
    # counts the occurance of the candidate
    def isMajority(self, A, cand):
        count = 0
        for i in range(len(A)):
            if A[i] == cand:
                count += 1
        if count > len(A)/2:
            return True
        else:
            return False
    
    def majorityElement(self, A,N):
        cand = self.findCandidate(A)
    
        # Print the candidate if it is Majority
        if self.isMajority(A, cand) == True:
            return cand
        else:
            return -1