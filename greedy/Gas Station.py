class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas)< sum(cost):
            return -1
        
        start_index = 0
        n = len(gas)
        diff = 0

        for i in range(n):
            diff += gas[i] - cost[i]
            if diff<0:
                start_index = i +1
                diff = 0


            
        return(start_index)  
   


            
        



        
