class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:


        ans = []

        def dfs(nums,k,path,ans):
            if k==0:
                ans.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[i+1:],k-1,path+[nums[i]],ans)

        nums = [i for i in range(1,n+1)]

        dfs(nums,k,[],ans)
        return ans            

