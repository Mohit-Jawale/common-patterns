import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        a =  heapq.nlargest(k,nums)
        return a[-1]

        
        
