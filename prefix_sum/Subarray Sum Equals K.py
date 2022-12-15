class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum = sum + nums[j]
        #         if sum == k:
        #             count+=1

        # return count

        count = 0
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        prev = 0
        for i in nums:
            prev = prev + i
            sum = prev - k
            if sum in lookup:
                count+=lookup[sum]
            lookup[prev]+=1
        return count
