#Question - https://practice.geeksforgeeks.org/problems/coin-change2448/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution:
    def count(self, coins, n, sum):
        table = [0 for k in range(sum+1)]
 
        table[0] = 1 #Base case
 
        for i in range(0, n):
            for j in range(coins[i], sum+1):
                table[j] += table[j-coins[i]]
 
        return table[sum]

#Time Complexity = O(n*sum)
