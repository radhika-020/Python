class Solution:
    def count(self, coins, N, Sum):
        # code here 
        if Sum == 0:
            return 1
        if Sum < 0:
            return 0
        if N<=0:
            return 0
            
        return self.count(coins, N-1, Sum) + self.count(coins, N, Sum - coins[N-1])
