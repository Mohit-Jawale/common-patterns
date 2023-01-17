from functools import lru_cache

#### THE below is DFS with MEMO solution is intution to the next DP soltuion where we calculated solution from the last node and move towards the first node of tree.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = {}

        def dfs(index,prev):
            nonlocal dp
            if index == len(nums):
                    return 0
            LIS = 0

            if index in dp:
                return dp[index]

            for i in range(index,len(nums)):
                if nums[i]>prev:
                    curr = 1+ dfs(i+1,nums[i])
                    LIS = max(curr,LIS)
            dp[index] = LIS
                    
            return LIS
            
        return dfs(0,-float("inf"))
    
    ###DP Solution
    class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        LIS= [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i]= max(LIS[i],1+LIS[j])
        
        return max(LIS)
    
      






        

        

        
