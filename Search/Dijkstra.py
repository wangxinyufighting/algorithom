import heapq.pqueue

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

def init_dist(graph, s):
    dist = {}
    for i in graph.keys():
        dist[i] = float('inf')
    dist[s] = 0

    return dist

def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set(s)
    distance = init_dist(graph, s)
    parent = {s:None}

    while pqueue:
        pair = heapq.heappop(pqueue)
        d = pair[0]
        v = pair[1]
        seen.add(v)

        nodes = graph[v].keys()
        for node in nodes:
            if node not in seen:
                if d + graph[v][node] < distance[node]:
                    heapq.heappush(pqueue, (d+graph[v][node], node))
                    parent[node] = v
                    distance[node] = d + graph[v][node]

    return parent, distance





