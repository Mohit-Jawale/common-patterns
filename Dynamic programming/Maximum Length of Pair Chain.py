class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs = sorted(pairs,key=lambda x:x[0])

        dp= [1] * len(pairs)

        for i in range(len(pairs)-1,-1,-1):
            for j in range(i+1,len(pairs)):
                if (pairs[i][1]<pairs[j][0]) and dp[i]<dp[j]+1:
                    dp[i] = 1+dp[j]

        return max(dp)            
