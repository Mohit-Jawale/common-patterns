class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:

        if len(s)<k:
            return len(s)

        i,j = 0,k-1
        max_len = j-i+1
        unique = set()
        while(j<len(s)):
            unique.update(s[i:j+1])
            if len(unique) <= k:
                max_len = max(max_len,j-i+1)
                
            elif len(unique)>k:
                while i <= j:
                    unique.clear()
                    i+=1
                    unique.update(s[i:j+1])
                    if len(unique)==k:
                        break
            j+=1                        

            
        return(max_len)        
