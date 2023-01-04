class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        unique = collections.defaultdict(int)
        for i in nums:
            unique[i]+=1
        ans = []    
        for i in unique.keys():
            ans.append([unique[i],i])

        a = heapq.nlargest(k,ans)
        real_ans = []
        for x,y in a:
            real_ans.append(y)
        
        return real_ans
