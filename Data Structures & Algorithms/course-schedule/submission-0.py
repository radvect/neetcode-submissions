class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {course: [] for course in range(numCourses)}
        for i in prerequisites:
            graph[i[1]].append(i[0])
        current_path = set()
        checked = set()

        def dfs(course):
            nonlocal checked
            nonlocal current_path

            if(course in current_path):
                return False
            if(course in checked):
                return True
            current_path.add(course)
            
            for i in range(len(graph[course])):
                stat = dfs(graph[course][i])
                if(not stat):
                    return False
            checked.add(course)
            current_path.remove(course)
            
            return True
        
        for i in graph.keys():
            if(dfs(i)):
                continue
            else:
                return False
        return True



