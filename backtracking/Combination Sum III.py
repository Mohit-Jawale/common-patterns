class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:




        ans = []

        def dfs(nums,target,k,path,ans):
            if k==0 and target == 0:
                ans.append(path)
                return
            if target<0:
                return 

            for i in range(len(nums)):
                dfs(nums[i+1:],target-nums[i],k-1,path+[nums[i]],ans)


        nums = [1,2,3,4,5,6,7,8,9]
        dfs(nums,n,k,[],ans)
        return ans  


        
