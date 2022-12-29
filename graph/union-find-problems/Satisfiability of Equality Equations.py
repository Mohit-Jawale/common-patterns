class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        n = 26
        root = [i for i in range(n)]
        rank = [1]*n


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
                    root[rootY] = rootX
                elif rank[rootY]> rank[rootX]:
                    root[rootX] = rootY
                else:
                    root[rootY]=rootX 
                    rank[rootX]+=1


        
        for i in equations:
            if i[1]=="=" and i[2]=='=':
                x = int(ord(i[0]))-97
                y = int(ord(i[3]))-97
                union(x,y)

        for i in equations:
            if i[1]=="!" and i[2]=='=':
                x = int(ord(i[0]))-97
                y = int(ord(i[3]))-97
                if find(x)==find(y):
                    return False

        return True            
                 
