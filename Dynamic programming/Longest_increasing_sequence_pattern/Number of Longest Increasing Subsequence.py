class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        dp = [1]*len(nums)
        count = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    if dp[i]< dp[j]+1:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i] == dp[j]+1:
                        count[i]+=count[j]

     

        # get the length of lonest increasing subsequence
        max_length = max(dp)
        print(dp,count)
        # report total path count of longest increasing subsequence
        ans = 0
        for length,count in zip(dp,count):
            if length == max_length:
                 ans+=count

        return ans
            
   
        
                    
                
        
                    
                    
                    
                    
        
        
