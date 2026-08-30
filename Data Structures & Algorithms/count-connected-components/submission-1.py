class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        num_of_components = 0
        visited = set()
        print(graph)
        
        def dfs(node, parent):
            print(node)
            if(node in visited):
                
                return False
            
            visited.add(node)
            statement = True 
            for i in range(len(graph[node])):
                if(parent == graph[node][i]):
                    continue
                statement&=dfs(graph[node][i],node)

            return statement

        for i in range(len(graph)):
            #print(graph[i])
            if(i in visited):
                continue
            else:
                num_of_components+=1
                dfs(i, -1)

        return num_of_components