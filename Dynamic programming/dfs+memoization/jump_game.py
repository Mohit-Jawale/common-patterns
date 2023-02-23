
class Solution:
    def canJump(self, nums: List[int]) -> bool:
       
        @lru_cache(None)
        def dfs(curr_idx):

            if curr_idx >= len(nums)-1:
                return True

            if nums[curr_idx] == 0:
                return False   

            for i in range(nums[curr_idx],0,-1):
                 if dfs(curr_idx+i):
                     return True
                  
                 
            return False
      


        return dfs(0)
