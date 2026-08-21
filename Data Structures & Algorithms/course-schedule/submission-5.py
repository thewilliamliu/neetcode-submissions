class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological order exists iff no directed cycles.

        # Adjacency list > matrix for better DFS time.
        graph = [[] for _ in range(numCourses)]
        state = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append((course))
        
        for course in range(numCourses):
            if not self.dfs(course, graph, state): return False

        return True
        
    
    # Need three states since marked is different than marked ON THAT PATH.
    def dfs(self, course, graph, state):
        if state[course] == 1:
            return False

        if state[course] == 2:
            return True

        if state[course] == 0:
            state[course] = 1
            
            for next_course in graph[course]:
                if not self.dfs(next_course, graph, state): return False
        
            state[course] = 2

            return True
        
            
    
            
        

        
        