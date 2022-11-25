class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums)==1:
            return [nums[:]] #Returning list of lists, for eg, [[1]].
        
        for i in range(len(nums)):
            n = nums.pop(0) #At the very first, popping or removing the very first element of the given array, and then calling permute function on the other left.
            perms = self.permute(nums)
            
            for j in perms: #Now for every element in the obtained perms, we are adding the element that we reemoved earlier to get the permutation string.
                j.append(n)
            result.extend(perms) #Adding the perms to our original result
            nums.append(n) #Adding the removed n to the original nums array to again perform backtracking on the same elements again.
            
        return result
