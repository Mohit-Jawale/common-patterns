class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        root = [i for i in range(n)]
        rank = [1]*n
        components = n

        def find(x):
            if x == root[x]:
                return x
            root[x]= find(root[x])
            return root[x]

        def union(x,y):
            nonlocal components
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return False
            if rootX != rootY:
                if rank[rootX]> rank[rootY]:
                    root[rootY]= rootX
                elif rank[rootY]> rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY]= rootX
                    rank[rootX]+=1
                components-=1    
            return True

        index = []
        for i,(x,y) in enumerate(connections):
            flag = union(x,y)
            if not flag:
                index.append(i)
        repeat_connection = len(index)
        
        if components-1 <= repeat_connection:
            return min(repeat_connection,components-1)
        else:
            return -1    
    
