class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        nums.sort()


        ans = []

        def dfs(nums,path,ans):
            
            ans.append(path)

            if not nums:
                return
            
            for i in range(len(nums)):
                dfs(nums[i+1:],path+[nums[i]],ans)

        dfs(nums,[],ans)
        return ans        
