# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        def trav(self,root):
            if not root:
                return 0
            return 1 + max(trav(self,root.left),trav(self,root.right))
        return trav(self,root)