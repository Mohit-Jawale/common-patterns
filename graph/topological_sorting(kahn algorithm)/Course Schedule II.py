class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj_list = collections.defaultdict(list)
        in_degree = [0] * numCourses
        for i,j in prerequisites:
            adj_list[j].append(i)
            in_degree[i]+=1

        queue = []
        for index,value in enumerate(in_degree):
            if value==0:
                queue.append(index)

        topo = []
        while queue:
            node = queue.pop(0)
            topo.append(node)
            for neighbour in adj_list[node]:
                in_degree[neighbour]-=1

                if in_degree[neighbour]==0:
                    queue.append(neighbour)

        if len(topo) == numCourses:
            return topo
        return []        
