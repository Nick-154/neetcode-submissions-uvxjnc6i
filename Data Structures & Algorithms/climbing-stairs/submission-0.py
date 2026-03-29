class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: if n is 1, answer is 1. 
        # We initialize two variables to represent the last two steps.
        # 'one' represents the number of ways to reach the current step.
        # 'two' represents the number of ways to reach the previous step.
        # Initial state represents n=0 and n=1, both having 1 'way' essentially
        # (standing at start is 1 way, reaching step 1 is 1 way).
        one, two = 1, 1
        
        # We loop n-1 times because we already have the base cases set up
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one