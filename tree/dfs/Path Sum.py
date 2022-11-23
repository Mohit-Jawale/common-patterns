class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:


        def path_sum(root,sum_remain):
            
            if root == None:
                return

            if root.left==None and root.right==None:
                if sum_remain-root.val == 0:
                    return True 
                else:
                    return False    

            left = path_sum(root.left,sum_remain-root.val)
            right= path_sum(root.right,sum_remain-root.val)

            if left or right:
                return True
            else:
                return False   

        return path_sum(root,targetSum)      
