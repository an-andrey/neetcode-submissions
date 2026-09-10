from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        queue = deque()

        combos = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        opening = ["(", "[", "{"]
        closing = [")", "]", "}"]

        for l in s:
            if l in opening: 
                queue.append(l)

            if l in closing: 
                if len(queue) == 0: 
                    return False
                
                o = queue.pop()

                if combos[l] != o:
                    return False
            
        if len(queue) == 0: 
            return True
        else: 
            return False


