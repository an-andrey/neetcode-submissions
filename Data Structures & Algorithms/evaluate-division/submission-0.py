from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        """
        Ex: 

        Know: 
        a/b = 4.0 --> a = 4*b && b = a/4.0
        b/c = 1.0 --> b = 1*c = c && c = b/1.00 = b
        ab / bc = 3.25 --> ab = 3.25*bc && bc = ab/3.25

        Want: 
        a/c = ?
        b/a = ?
        c/c = ?
        ab/a = ?
        d/d = ?

        Build out a computation graph and traverse it
        """

        vars = {}

        class ComputeNode: 
            def __init__(self, var: str):
                self.var = var
                self.children = {}

            def add_eqn(self, var, val):
                self.children[var] = val

        def dfs(root, target): 
            seen = set()
            seen.add(root)
            stack = deque([(root, 1)])

            while stack: 
                (node, product) = stack.pop()

                if node.var == target: 
                    return product

                for c, c_val in node.children.items(): 
                    if c in seen: 
                        continue

                    seen.add(c)
                    stack.append((c, product*c_val))
                
            return -1


        for ((a, b), v) in zip(equations, values): 
            if a not in vars:
                vars[a] = ComputeNode(a)
            if b not in vars: 
                vars[b] = ComputeNode(b)

            vars[a].add_eqn(vars[b], 1/v)
            vars[b].add_eqn(vars[a], v)

        output = []
        for (a, b) in queries: 
            if a not in vars or b not in vars: 
                output.append(-1)
                continue
            
            output.append(dfs(vars[b], a))

        return output
            






