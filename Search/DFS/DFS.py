graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}

#用栈实现深度优先搜索
def DFS(graph, s):
    stack = [s]
    seen = set(s)

    while stack:
        s = stack.pop()
        nodes = graph[s]
        for node in nodes:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(s)


DFS(graph, 'A')