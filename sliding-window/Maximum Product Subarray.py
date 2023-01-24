class Solution:
    def maxProduct(self, nums: List[int]) -> int:

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
