# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)
        
    def validate(self, root, min_val = None, max_val = None): 
        if root is None: 
            return True

        if min_val is not None: 
            if min_val >= root.val: 
                return False

        if max_val is not None: 
            if max_val <= root.val: 
                return False

        return self.validate(root.right, root.val, max_val) and self.validate(root.left, min_val, root.val)
        

    