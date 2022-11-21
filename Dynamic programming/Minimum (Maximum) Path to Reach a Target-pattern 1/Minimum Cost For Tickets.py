from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        def find_next_index(index,n):

            if n==7:
                num = days[index]+7-1
                for i in range(index,len(days)):
                    if days[i]>num:
                        return i
                return len(days)        
            elif n==30:
                num = days[index]+30-1
                for i in range(index,len(days)):
                    if days[i]>num:
                        return i      
                return len(days)         
            
        @lru_cache(None)
        def frugal_journey(index):
            if index >=len(days):
                return 0


          
            cost_1 = costs[0]+frugal_journey(index+1)

            cost_7  = costs[1]+frugal_journey(find_next_index(index,7))

            cost_30 = costs[2]+frugal_journey(find_next_index(index,30))


            result = min(cost_1,cost_7,cost_30) 

            return result


        return frugal_journey(0)
