#####see how the index is used to group the componenets

class Solution:
    def removeStones(self, points):
        
        n = len(points)
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

            if rootX != rootY:
                if rank[rootX]> rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootY]> rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY]=rootX 
                    rank[rootX]+=1
                components-=1    


        row_prev = {}
        col_prev = {}

        for i in range(n):
            row = points[i][0]
            col = points[i][1]
            if row in row_prev:
                union(i,row_prev[row])
            if col in col_prev:
                union(i,col_prev[col])
            row_prev[row]= i
            col_prev[col]= i  


        return(n-components)


