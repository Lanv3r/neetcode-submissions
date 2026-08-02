"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes = {}
        processed = set()
        if node is None:
            return None
        q = deque([node])
        while q:
            n = q.popleft()
            val, neighbors = n.val, n.neighbors
            if val in processed:
                continue
            if val not in nodes:
                nodes[val] = Node(val, [])
            
            if neighbors is not None:
                for neighbor in neighbors:
                    if neighbor.val in processed:
                        nodes[val].neighbors.append(nodes[neighbor.val])      
                        continue    
                    if neighbor.val not in nodes:
                        nodes[neighbor.val] = Node(neighbor.val, [])
                    nodes[val].neighbors.append(nodes[neighbor.val])  
                    q.append(neighbor)
                        
            processed.add(val)

        return nodes[1]