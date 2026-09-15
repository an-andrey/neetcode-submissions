# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        while True: 
            if p.val <= root.val and root.val <= q.val: 
                return root
            
            else: 
                if p.val <= root.val:
                    root = root.left
                else: 
                    root = root.right

        return None

            