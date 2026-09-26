class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: 
            return False

        adj = [[] for _ in range(n)]

        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)

        visiting = set()

        def has_cycle(root, parent):
            if root in visiting: 
                return True
            
            visiting.add(root)

            for node in adj[root]: 
                if node == parent: 
                    continue
                if has_cycle(node, root): 
                    return True

            return False

        if has_cycle(0, -1): 
            return False
        
        return n == len(visiting)
        


            


