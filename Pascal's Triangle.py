class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]] """The very irst row, 2-D Array, as required in output [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"""
        
        for i in range(numRows - 1): """numRows -1 because one row is already initialised in the beginning, i.e., [[1]]"""
            temp = [0] + res[-1] + [0] """Added [0] on both the sides of the previous row because Pascal triangle is the sum of the above two numbers, therefore, for the starting 1 in the next row, previous row's [0] and [1] is used and similarly for the ending 1."""
            row = []
            for j in range(len(res[-1]) + 1): """The other loop is iterated till length of the previous row which will be achieved by res[-1] + 1 as we can see, that the 3rd row contains 3 columns, one more than the previous one, and similary for the rest of the rows."""
                row.append(temp[j] + temp[j+1]) """Appended i.e., added in the row the j value and j + 1 value """
            res.append(row)
        return res
        
        
""" Pascal Triangle is a triangle containing n number of rows, where n is the input by the user and each number in the next row is the sum of the above two numbers."""
        
