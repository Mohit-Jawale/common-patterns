class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        lds = [[num] for num in nums]
        

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]%nums[i]==0 and len(lds[i]) <len(lds[j])+1:
                    lds[i]= [nums[i]] + lds[j]
             
                    
        return(max(lds,key=len))       
                    
                
                 
