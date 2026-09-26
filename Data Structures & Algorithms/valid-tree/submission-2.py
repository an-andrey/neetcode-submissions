class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]

        for e in edges: 
            n1, n2 = e[0], e[1]
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        visiting = set()

        def has_cycle(root):
            if root in visiting: 
                return True
            
            visited.add(root)
            visiting.add(root)

            for node in adj[root]: 
                adj[node].remove(root)
                if has_cycle(node): 
                    return True
            
            adj[root] = [] # clear passed neighbours
            visiting.remove(root)
            return False

        if has_cycle(0): 
            return False
        
        return n == len(visited)
        


            


