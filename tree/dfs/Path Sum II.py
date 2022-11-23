# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
            queue = []
            ans = []

            def find_path(root,remaining_sum):
                nonlocal queue
                nonlocal ans

                if root is None:
                    return
                if root.left == None and root.right == None:
                    if root.val - remaining_sum == 0:
                        queue.append(root.val)
                        ans.append(copy.deepcopy(queue))
                        queue.pop()
                        return True
                    else:
                        return False
                        
                queue.append(root.val)
                left = find_path(root.left,remaining_sum-root.val)
                right = find_path(root.right,remaining_sum-root.val)
       
                if left or right:
                    queue.pop()
                    return True
                else:
                    queue.pop()
                    return False          

            find_path(root,targetSum)
            return(ans)      

