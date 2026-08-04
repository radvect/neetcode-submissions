# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        qu = []
        level = len(qu)
        if(root is not None):
            qu.append(root)
        else: 
            return []
        while(len(qu)>0):
            level_ls = []
            level = len(qu)
            for i in range(level):
                if(qu[0].left is not None):
                    qu.append(qu[0].left)
                if(qu[0].right is not None):
                    qu.append(qu[0].right)
                temp = qu.pop(0)
                level_ls.append(temp.val)
            res.append(level_ls)
            
        return res

            




