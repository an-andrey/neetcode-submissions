# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def _in_order(root):
            nonlocal count
            if root.left: 
                res = _in_order(root.left)
                if res != -1: 
                    return res

            count += 1
            if count == k: 
                return root.val

            if root.right: 
                res = _in_order(root.right)
                if res != -1: 
                    return res

            return -1

        return _in_order(root)

            

            
            



            
            