class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSubArray = nums[0]
        sum = 0
        
        for n in nums:
            if sum < 0:
                sum = 0
            sum = sum + n
            maxSubArray = max(sum, maxSubArray)
        return maxSubArray
        
        
        
"""Question - Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6, i.e., fond the substring with the largest sum."""
