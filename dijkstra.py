def dijkstra(graph, n, source):
    dist = [float('inf')] * n
    visited = [False] * n
    
    dist[source] = 0
    
    for _ in range(n):
        min_dist = float('inf')
        u = -1
        
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        
        visited[u] = True
        
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]
    
    return dist


graph = [
    [0,4,1,0,0],
    [4,0,2,5,0],
    [1,2,0,3,0],
    [0,5,3,0,1],
    [0,0,0,1,0]
]

print(dijkstra(graph, 5, 0))
