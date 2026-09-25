class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:    
        nodes = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:         
            nodes[course].append(prereq)
        
        visiting = set()
        def has_cycle(course) -> bool:
            if course in visiting: 
                return True # looped back

            if not nodes[course]: # if explored everything
                return False
            
            visiting.add(course)
            for p in nodes[course]: 
                if has_cycle(p): 
                    return True

            visiting.remove(course)
            nodes[course] = [] # empty to show it's good

            return False

        for i in range(numCourses): 
            if has_cycle(i): 
                return False
        return True
