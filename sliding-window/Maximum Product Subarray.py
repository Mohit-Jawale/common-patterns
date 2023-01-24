class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        #### This is not same as other sliding window problem however there are total 3 cases you should think -:
        #### 1) Array has only positive numbers
        #### 2) Array has zero as partition
        #### 3) Array has negative and postive number.

        i,j = 0 ,0 
        product = 1
        max_product = nums[0]
        while j <=len(nums):
            if j<len(nums) and nums[j]!=0 :
                product = product*nums[j]
                max_product = max(max_product,product)
            else:
                while(i<j-1):
                    product = product//nums[i]    
                    if product>max_product:
                        max_product = product
                    i+=1   
                product = 1
                i = j+1
                if j< len(nums):
                    max_product = max(0,max_product)
   
            j+=1

        return max_product    
