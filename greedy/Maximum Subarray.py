class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        total = 0
        ans = -float('inf')
        for i in range(len(nums)):
            total = total+nums[i]
            if ans<total:
                ans = total
            if total<0:
                total = 0
           
        return ans            


