#Question - https://practice.geeksforgeeks.org/problems/coin-change2448/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution:
    def count(self, coins, N, Sum):
        if Sum == 0:
            return 1
        if Sum < 0:
            return 0
        if N<=0:
            return 0
            
        return self.count(coins, N-1, Sum) + self.count(coins, N, Sum - coins[N-1])
    
#Time Complexity = O(N^Sum)
