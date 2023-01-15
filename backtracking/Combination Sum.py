import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        

        ans = []
        def dfs(nums,target,path,ans):

            if target<0:
                return False
            if target==0:
                ans.append(path)
                return

            for i in range(len(nums)):
                print(nums[i:])
                dfs(nums[i:],target-nums[i],path+[nums[i]],ans)
           

        dfs(candidates,target,[],ans)
    
        return ans
        
