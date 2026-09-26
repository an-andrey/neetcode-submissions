class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cc = 0 
        
        adj = [[] for _ in range(n)]

        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        def dfs(root, parent): 
            visited.add(root)
            for node in adj[root]: 
                if node in visited: 
                    continue
                dfs(node, root)

        for i in range(n): 
            if i not in visited: 
                cc += 1
                dfs(i, -1)

        return cc

        
        