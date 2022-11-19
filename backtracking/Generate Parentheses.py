import copy
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_bracket = '('
        close_bracket = ')'
        ans = []

        def check_paranthethis(s):
            stack = []
            
            for i in range(len(s)):
                if s[i] == open_bracket:
                    stack.append(s[i])
                else:
                    if not stack and s[i]==close_bracket:
                        return False
                    a = stack.pop(0)  
                    if a==s[i]:
                        return False
            if stack:
                return False
            return True

        def generate_brackets(s):
            if len(s)==n*2:
                if check_paranthethis(s):
                    ans.append(copy.deepcopy(s))
                return

            for i in ['()',')(','((','))']:
                s = list(s)
                middle = len(s)//2
                front = "".join(s[0:middle])
                end  = "".join(s[middle:len(s)])
                s = front+i+end
                generate_brackets(s)
                s = front + end
            return

        generate_brackets("()")
        return(ans)        


                

