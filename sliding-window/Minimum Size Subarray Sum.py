class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j = 0,0
        min_len = 999999999
        window_sum = 0
        len_ar = len(nums)
        while(j<len_ar):
            window_sum += nums[j]
            if window_sum>=target:
                min_len = min(min_len,j-i+1)
                while(i<=j):
                    window_sum = window_sum - nums[i]
                    i+=1
                    if window_sum>=target:
                        min_len = min(min_len,j-i+1)
                    else:
                        break      
            j+=1
                

        if min_len == 999999999:
            return 0
        return min_len    
