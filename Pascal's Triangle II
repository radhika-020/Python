"""Same as the Pascal's Triangle problem, only diffrence is, here, we have to return the elements of the inputted row number, for example, rowIndex = 3, then the output will be [1, 3, 3, 1]."""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]*(rowIndex +1) """because the output rows will be one greater than the input rows"""
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] = result[j]+result[j-1]
        return result
        
