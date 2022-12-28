
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)+1
        root = [i for i in range(n)]
        rank = [1] * n
        ans = []
        


        def find(x):
            if x == root[x]:
                return x
            root[x]= find(root[x])
            return root[x]


        def union(x,y):

            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]> rank[rootY]:
                    root[rootY]=rootX

                elif rank[rootY]> rank[rootX]:
                    root[rootX] = rootY
                    
                else:
                    root[rootY]=rootX
                    rank[rootX]+=1
                
            else:
                ##### This helps to detect cycle in the graph
                return True
         

        for i,j in edges:
            
            if union(i,j):
                ans = [i,j]
                break

        return ans        
