graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

#用队列实现广度优先搜索
def BFS(graph, s):
    queue = [s]
    seen = set(s)
    parent = {}
    while queue:
        s = queue.pop(0)
        nodes = graph[s]
        for node in nodes:
            if node not in seen:
                queue.append(node)
                seen.add(node)
                parent[node] = s
        print(s)


