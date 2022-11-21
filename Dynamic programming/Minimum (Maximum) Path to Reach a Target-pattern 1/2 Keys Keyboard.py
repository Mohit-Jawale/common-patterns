from functools import lru_cache
class Solution:
    def minSteps(self, n: int) -> int:
            visited = set()

            @lru_cache(None)
            def print_min(screen,store):

                if len(screen)==n:
                    return 0

                if len(screen)>n:
                    return 999999999    
                if (screen,store) in visited:
                    return 999999999
                else:
                    visited.add((screen,store))  

                copy = 1+print_min(screen,screen)
                paste = 1+print_min(screen+store,store)
                result = min(copy,paste)
                return  result       



            return print_min("A","")






                
