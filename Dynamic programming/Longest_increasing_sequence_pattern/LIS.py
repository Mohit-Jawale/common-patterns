from functools import lru_cache
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
      






        

        

        
