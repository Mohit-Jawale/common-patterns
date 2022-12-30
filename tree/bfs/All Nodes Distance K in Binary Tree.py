# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        lookup_parent = collections.defaultdict(list)

        def dfs(node,parent):
            if node == None:
                return
            if parent>=0:
                lookup_parent[node.val].append(parent)
                lookup_parent[parent].append(node.val)
            dfs(node.left,node.val)
            dfs(node.right,node.val)
            
            return    

        def get_the_kth_elements(target_node,t):
            nonlocal ans
            queue = []
            seen = set()
            queue.append((target_node,t))
            seen.add(target_node)
            while queue:
                node,level = queue.pop(0)

                if level==k:
                    ans.append(node)

                for neighnour in lookup_parent[node]:
                    if neighnour not in seen:
                        seen.add(neighnour) 
                        queue.append((neighnour,level+1))

                    

        ans = []
        dfs(root,-1)
        get_the_kth_elements(target.val,0)
        return(ans)



        

            
