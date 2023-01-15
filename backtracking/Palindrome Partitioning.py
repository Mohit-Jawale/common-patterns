class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s)==1:
            return[[s]]


        def check_palindrome(s):
            i,j=0,len(s)-1
            while(i<=j):
                if s[i]==s[j]:
                    i+=1
                    j-=1
                    pass
                else:
                    return False

            return True  

        ans = []
        partion = []
        def dfs(i):
            if i==len(s):
                ans.append(copy.deepcopy(partion))
                return
            for j in range(i,len(s)):
                if check_palindrome(s[i:j+1]):
                    partion.append(s[i:j+1])
                    dfs(j+1)
                    partion.pop()

        dfs(0)
        return ans            

            
                


        get_palidrome_substring(s)
        return ans
