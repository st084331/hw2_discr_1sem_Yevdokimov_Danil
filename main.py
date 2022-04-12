def bfs(graph, new_graph, source, sink):
    hgraph = [source]
    paths = {source: []}
    if source == sink:
        return paths[source]
    while (hgraph):
        u = hgraph.pop()
        for v in range(len(graph)):
            if (graph[u][v] - new_graph[u][v] > 0) and v not in paths:
                paths[v] = paths[u] + [(u, v)]
                if v == sink:
                    return paths[v]
                hgraph.append(v)
    return None

def bfs_for_dinic(graph, new_graph, source, sink):
    rows = len(graph)
    queue = []
    queue.append(source)
    global level
    level = rows * [0]
    level[source] = 1
    while queue:
        k = queue.pop(0)
        for i in range(rows):
            if (new_graph[k][i] < graph[k][i]) and (level[i] == 0):  # not visited
                level[i] = level[k] + 1
                queue.append(i)
    return level[sink] > 0

def dfs_for_dinic(graph, new_graph, search, capacity):
    current = capacity
    if search == len(graph) - 1:
        return capacity
    for i in range(len(graph)):
        if (level[i] == level[search] + 1) and (new_graph[search][i] < graph[search][i]):
            f = dfs_for_dinic(graph, new_graph, i, min(current, graph[search][i] - new_graph[search][i]))
            new_graph[search][i] = new_graph[search][i] + f
            new_graph[i][search] = new_graph[i][search] - f
            current = current - f
    return capacity - current

def Ford_Fulkerson(graph, source, sink):
    rows = len(graph)
    new_graph = [[0] * rows for i in range(rows)]
    path = bfs(graph, new_graph, source, sink)
    while path != None:
        flow = min(graph[u][v] - new_graph[u][v] for u, v in path)
        for u, v in path:
            new_graph[u][v] += flow
            new_graph[v][u] -= flow
        path = bfs(graph, new_graph, source, sink)
    return sum(new_graph[source][i] for i in range(rows))

def Edmonds_Karp(graph, source, sink):
    rows = len(graph)
    new_graph = [[0] * rows for i in range(rows)]
    path = bfs(graph, new_graph, source, sink)
    while path != None:
        flow = min(graph[u][v] - new_graph[u][v] for u, v in path)
        for u, v in path:
            new_graph[u][v] += flow
            new_graph[v][u] -= flow
        path = bfs(graph, new_graph, source, sink)
    return sum(new_graph[source][i] for i in range(rows))

def Dinic(graph, source, sink):
    rows = len(graph)
    new_graph = [rows * [0] for i in range(rows)]
    flow = 0
    while (bfs_for_dinic(graph, new_graph, source, sink)):
        flow = flow + dfs_for_dinic(graph, new_graph, source, 100000)
    return flow

graph = [[0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

graph[0][1] = 7
graph[0][2] = 4
graph[1][2] = 4
graph[1][3] = 2
graph[2][4] = 4
graph[3][4] = 4
graph[3][5] = 5
graph[4][5] = 12
graph[2][3] = 8

for i in range(len(graph)):
    for j in range(len(graph)):
        print(graph[i][j], end=", ")
    print()

print(Edmonds_Karp(graph, 0, len(graph) - 1))
print(Ford_Fulkerson(graph, 0, len(graph) - 1))
print(Dinic(graph, 0, len(graph)-1))