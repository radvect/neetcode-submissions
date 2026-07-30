# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if(p is None and q is None):
            return  True
        elif((p is None) or (q is None)):
            return False
        elif(p.val!=q.val):
            return False
        elif(p.val==q.val):
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if(root is None):
            return False
        elif(root is not None):
            if(self.sameTree(root, subRoot)):
                return True 
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        