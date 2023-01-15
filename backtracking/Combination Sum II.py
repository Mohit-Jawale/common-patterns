class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans= []
        candidates.sort()


        def dfs(nums,target,path,ans):
            if target<0:
                return
            if target == 0:
                ans.append(path)
                return

            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[i+1:],target-nums[i],path+[nums[i]],ans)        


        dfs(candidates,target,[],ans) 
        return(ans)       
