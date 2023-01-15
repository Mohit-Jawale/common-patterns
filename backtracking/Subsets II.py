class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        def dfs(nums,path,ans):
            ans.append(path)
            if not nums:
                return

            for i in range(len(nums)):

                if i>0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[i+1:],path+[nums[i]],ans)

        dfs(nums,[],ans)
        return ans             
