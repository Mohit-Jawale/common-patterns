class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        N = len(nums)

        def dfs(nums,path,ans):
            nonlocal N
            if len(path)==N:
                ans.append(path)
                return
            
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:],path+[nums[i]],ans)
    

        dfs(nums,[],ans)
        return ans
