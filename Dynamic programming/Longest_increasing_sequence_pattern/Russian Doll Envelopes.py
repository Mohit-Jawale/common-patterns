class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        nums = sorted(envelopes,key=lambda x :(x[0], -x[1]))

        dp = [1]*len(nums)
        res = 1
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if (nums[i][0]<nums[j][0] and nums[i][1]<nums[j][1]) and dp[i]<dp[j]+1:
                    dp[i] = 1 + dp[j]
                if res<dp[i]:
                    res = dp[i]    

        return(res)            
