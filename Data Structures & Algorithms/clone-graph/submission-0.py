"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # start_Node = Node(node.val, )
        hash_table = dict()

        def dfs(node):
            if(node is None):
                return
            if(node in hash_table):
                return hash_table[node]
            
            new_node = Node(node.val,[])

            hash_table[node] = new_node 
             
            for i in range(len(node.neighbors)):
                new_node.neighbors.append(dfs(node.neighbors[i]))
            return new_node
        

        return dfs(node)