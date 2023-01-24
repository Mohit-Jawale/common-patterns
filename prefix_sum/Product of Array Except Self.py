class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = []
        prefix.append(1)
        suffix = collections.deque()
        suffix.append(1)
        suffix_num = 1
        

        for i in range(len(nums)-1):
            num = prefix[i]*nums[i]
            prefix.append(num)

        for i in range(len(nums)-1,0,-1):
            suffix_num = suffix_num*nums[i]
            suffix.appendleft(suffix_num)

        for i in range(len(prefix)):
            prefix[i] = prefix[i]*suffix[i]  

        return prefix        
