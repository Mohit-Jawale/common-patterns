class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        def find_distance(x,y):
           a =  pow(x-0,2)
           b = pow(y-0,2)
           return math.sqrt(a+b)

        distance = []
        for x,y in points:
            distance.append((find_distance(x,y),[x,y]))


        ans = heapq.nsmallest(k,distance)  
        real_ans = []
        for x,y in ans:
            real_ans.append(y)

        return real_ans    

