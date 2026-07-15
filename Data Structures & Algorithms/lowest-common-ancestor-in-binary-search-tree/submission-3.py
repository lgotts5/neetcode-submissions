# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #basicallly find when canidate is between numbers
        candidate = root
        if q.val > p.val:
            while not (candidate.val >= p.val and candidate.val <=q.val):
                if candidate.left and candidate.val > q.val:
                    candidate = candidate.left
                elif candidate.right:
                    candidate = candidate.right
        else:
            while not (candidate.val >= q.val and candidate.val <=p.val):
                if candidate.left and candidate.val > p.val:
                    candidate = candidate.left
                elif candidate.right:
                    candidate = candidate.right
        return candidate


        