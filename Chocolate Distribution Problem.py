#Question - https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

class Solution:

    def findMinDiff(self, arr,n,m):
      #n is no. of packets of chocolates
      #m is no. of students

        if (n==0 or m==0):
            return 0
        arr.sort()
        if (n<m): #No. of students cannot be more than no of students.
            return -1
        
        min_diff = arr[n-1] - arr[0]
        
        for i in range(len(arr)-m+1): #Loop goes till m(+1 because Python works for 1 lesser value than specified in the loop)
            min_diff = min(min_diff, arr[i+m-1]-arr[i])
        
        return min_diff
            
