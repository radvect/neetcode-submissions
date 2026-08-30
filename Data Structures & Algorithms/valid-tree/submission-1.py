class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = {i:[] for i in range(n)}

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
            
        visited=set()

        def dfs(node, graph, skip_node):
            print(node)
            
            if(node in visited):
                #print(node)
                return False

            visited.add(node)
            statement = True
            for i in range(len(graph[node])):
               
                if(graph[node][i]==skip_node):
                    continue
                else:
                    statement=statement and dfs(graph[node][i],graph, node)
            print(node, statement)
           

            return statement


        return dfs(0, graph, -1) and len(visited) == n