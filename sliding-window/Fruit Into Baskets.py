class Solution:
    def totalFruit(self, fruits: List[int]) -> int:


        seen = collections.defaultdict(int)

        i ,j = 0 ,0
        max_fruits = 0
        while j<len(fruits):
            seen[fruits[j]]+=1
            if len(seen)<=2:
                max_fruits = max(max_fruits,j-i+1)
            elif len(seen)>2:
                seen[fruits[i]]-=1
                if seen[fruits[i]]==0:
                    del seen[fruits[i]]
                i+=1
                while i<=j:
                    if len(seen)==2:
                        break
                    else:
                        seen[fruits[i]]-=1
                        if seen[fruits[i]]==0:
                            del seen[fruits[i]]
                        i+=1    

            j+=1
        return max_fruits    
