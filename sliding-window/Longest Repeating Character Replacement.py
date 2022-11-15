class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s)<k:
            return len(s)

        max_letter = ""
        max_len = 0

        i,j = 0 ,0
        counter_window = Counter()
        while(j<len(s)):
            counter_window[s[j]]+=1
            if (j-i+1)-max(counter_window.values()) <= k:
                max_len = max(max_len,j-i+1)
            else:
                counter_window[s[i]]-=1
                i+=1
                while(i<=j):
                    if (j-i+1)-max(counter_window.values())>k:
                        counter_window[s[i]]-=1
                        i+=1
                    else:
                        break    
       
            j+=1
            
            
        return max_len        
