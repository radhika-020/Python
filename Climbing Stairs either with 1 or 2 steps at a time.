class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1 
        """base case, i.e., 5 and 4th steps are initialised as 1 if n = 5, then the sequence would be 1, 1, 2, 3, 5, 8, everytime adding the previous two, just like in the Fibonacci Series. This is a DP approach. this could also be solved using recursion with a time complexity of 2^n, or using memoization with a time complexity of O(n). """
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        
        """for reference, 8, 5, 3, 2, 1, 1, a(one) = 1(last 1), b(two) = 1(last second 1)"""
        
