class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:


        def dfs(start):

            path_len = 0
            stack = []
            stack.append((start,path_len))
            seen = set()
            ans = (start,0)
            while stack:
                node, path_len  = stack.pop()

                if int(ans[1])<=path_len:
                    ans = (node,path_len)   

                if node in seen:
                    continue
                seen.add(node)    

                for neighbour in adj_list[node]:
                    if neighbour not in seen:
                        stack.append((neighbour,path_len+1))

            return ans        
                    


        adj_list = collections.defaultdict(list)

        for x,y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        ans = 0
        ans,distance_1 = dfs(0)
        ans,distance_2 = dfs(ans)
        return(distance_2) 

                  
