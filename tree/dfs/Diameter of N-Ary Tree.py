"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


########### Note -> never apply dfs or bfs on graph val unless and until its mentioned they are unique

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        adj_list = collections.defaultdict(list)
        def dfs(root):
            path_len = 0
            stack = [root]
            seen = set()
            max_path = 0
            nonlocal adj_list
            while stack:
                node = stack.pop()
                if node in seen:
                    continue
                seen.add(node)

                for neighbour in node.children:
                    if neighbour not in seen:
                        adj_list[node].append(neighbour)
                        adj_list[neighbour].append(node)
                        stack.append(neighbour)    


        def find_diameter(start):

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

        dfs(root)
        next_node,dia_1= find_diameter(root)
        next_node,dia_2 = find_diameter(next_node)
        return(dia_2)
        

