class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n= len(accounts)
        root = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            if x == root[x]:
                return x
            root[x]= find(root[x]) 
            return root[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                if rank[rootX]>rank[rootY]:
                    root[rootY]=rootX
                elif rank[rootY]> rank[rootX]:
                    root[rootX] = rootY 
                else:
                    root[rootY]= rootX
                    rank[rootX]+=1


        lookup_dict = {}

        for i in range(n):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in lookup_dict:
                    lookup_dict[accounts[i][j]]= i
                else:
                    union(i,lookup_dict[accounts[i][j]])

                    
        index_list = collections.defaultdict(list)
        for i in range(n):
            index_list[find(i)].append(accounts[i])



        ans = []

        for email in index_list.values():
            temp = set()
            name = email[0][0]
            for i in email:
                for j in range(1,len(i)):
                    temp.add(i[j])
            ans.append([name] + sorted(list(temp)))

        return ans            
                    

