# Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward 
# from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
# Find the minimum number of jumps to reach the end of the array (starting from the first element). 
# If an element is 0, then you cannot move through that element.

# Note: Return -1 if you can't reach the end of the array.

# Example 1
# Input:
# N = 11 
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
# Output: 3 
# Explanation: 
# First jump from 1st element to 2nd 
# element with value 3. Now, from here 
# we jump to 5th element with value 9, 
# and from here we will jump to the last. 

# Example 2 
# Input :
# N = 6
# arr = {1, 4, 3, 2, 6, 7}
# Output: 2 
# Explanation: 
# First we jump from the 1st to 2nd element 
# and then jump to the last element.

def minJumps(arr, n):
    if len(arr) <= 1 :
        return 0
    # Return -1 if not possible to jump
    if arr[0] == 0 :
        return -1 # First element 0 means no jump
    
    # Initialization
    maxReach = arr[0]
    steps = arr[0]
    jump = 1
    for i in range(1, len(arr)):
        # check if we have reached the end of array
        if i == len(arr) - 1 :
            return jump
        # Updating maxReach
        maxReach = max(maxReach, i+arr[i])

        # We use a step to get to the current index
        steps -= 1

        # If no further steps left
        if steps == 0:

            # We must have used a jump
            jump += 1

            #Check if the current index/position  or lesser index 
            #is the maximum reach point from the previous indexes 
            if i>= maxReach:
                return -1
            
            #re-initialize the steps to the amount 
            #of steps to reach maxReach from position i. 
            steps = maxReach - i
        
    return -1

arr = [1,4,3,2,6,7]
N = 6
print(minJumps(arr, N))

# Complete Solution:

# 1. if n <= 1, then return 0, because that is the destination
# 2. If arr[0] == 0 then return -1 as answer (no jumps are possible)
# 3. Now, Initialize maxrange and steps with arr[0], and jumps with 1 (as 1 jump will be required)
# 4. Now, starting iteration from index 1, the above values are updated as follows:
    # 1. First we test whether we have reached the end of the array, in that case we just need to return the jump variable
    # if (i == arr.length - 1) return jump;

    # 2. Next we update the maxrange. This is equal to the maximum of maxrange and i+arr[i](the number of steps we can take from the current position).
    # maxrange = max(maxrange,i+arr[i]);
    
    # 3. We used up a step to get to the current index, so steps has to be decreased.
    # step--;

    # 4. If no more steps are remaining (i.e. steps=0, then we must have used a jump. Therefore increase jump. Since we know that it is possible to reach 
    # maxrange, we again initialize the steps to the number of steps to reach maxReach from position i. But before re-initializing step, we also check 
    # whether a step  is becoming zero or negative. In this case, It is not possible to reach further.
    # if (step == 0) {
    #     jump++;
    #     if(i>=maxReach)
    #        return -1;
    #     step = maxReach - i;
    # }
# 5. Print the returned value