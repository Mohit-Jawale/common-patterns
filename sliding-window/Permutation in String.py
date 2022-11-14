### This solution has complexity of O(26*n) but its easier to understand.
### There is one more soltuion which is optimal ans has complexity O(o).

### Solution 1
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter_s1 = Counter(s1)
        i=0
        window_size = len(s1)
        while(i<len(s2)-window_size+1):
            counter_s2 = Counter(s2[i:i+window_size])
            if counter_s1 == counter_s2:
                return True
            i+=1

### Soltuion 2
