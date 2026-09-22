"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: 
            return node

        seen_nodes = {} 

        def helper(curr_head): 
            if curr_head in seen_nodes: 
                return seen_nodes[curr_head]
            
            curr_head_clone = Node(curr_head.val)
            seen_nodes[curr_head] = curr_head_clone

            for n in curr_head.neighbors: 
                curr_head_clone.neighbors.append(helper(n))

            return curr_head_clone

        return helper(node)