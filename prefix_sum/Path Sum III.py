# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        


        # count = 0    

        # def find_sum_path(node,total):
        #     nonlocal count
            
        #     if node == None:
        #         return
         
        #     find_sum_path(node.left,total + node.val)
        #     find_sum_path(node.right,total + node.val)

        #     if node.val + total == targetSum:
        #         count+=1


        # def inorder(root):
        #     if root ==None:
        #         return
        #     find_sum_path(root,0)
        #     inorder(root.left)
        #     inorder(root.right)
        #     return

        # inorder(root)
        # return count

        count = 0
        lookup = collections.defaultdict(int)
        prefix_sum = 0

        def dfs(root,prefix_sum):
            nonlocal count

            if root == None:
                return

            prefix_sum+=root.val  

            if prefix_sum == targetSum:
                count+=1

            count += lookup[prefix_sum-targetSum]

            lookup[prefix_sum]+=1  

            dfs(root.left,prefix_sum)
            dfs(root.right,prefix_sum)

            lookup[prefix_sum]-=1


        dfs(root,0)
        return(count)        






