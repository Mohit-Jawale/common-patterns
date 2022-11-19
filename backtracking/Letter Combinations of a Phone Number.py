import copy
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
                '2':"abc",
                '3':"def",
                '4':"ghi",
                '5':"jkl",
                '6':"mno",
                '7':"pqrs",
                '8':"tuv",
                '9':"wxyz"
        }  
        ans = []

        def decode_combination(s,start):
            if len(s) == len(digits):
                ans.append(copy.deepcopy(s))
                return
            for i in range(start,len(digits)):
                start+=1
                for j in mapping[digits[i]]:
                    s+=j
                    decode_combination(s,start)
                    s = s[:-1]
                s=""    
            return

            
        decode_combination("",0)
        if "" in ans:
            return []
        return(ans)
        



