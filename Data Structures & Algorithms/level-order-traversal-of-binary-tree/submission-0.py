# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def bfs(root, d): 
            if not root: 
                return

            if len(output)-1 < d: 
                output.append([root.val])
            else:
                output[d].append(root.val)

            bfs(root.left, d+1)
            bfs(root.right, d+1)

        bfs(root, 0)
        return output
