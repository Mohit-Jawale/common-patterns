import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        def backtrack(num):

            if len(num)==len(nums):
                ans.append(copy.deepcopy(num))
                return

            for i in list(set(nums)-set(num)):
                num.append(i)
                backtrack(num)
                del num[-1]
            return
        
        for i in nums:
            backtrack([i])

        return(ans)    
