# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(node):
            if(not node):
                return 0 
            nonlocal ans

            leftH = dfs(node.left)
            rightH = dfs(node.right)

            if(abs(leftH-rightH)>1):
                ans = False    
            
            return 1+ max(leftH, rightH)
        dfs(root)


        return ans
        
        