from collections import deque

def bfs(adjs, node_num, start, end):
    visited = [-1]*node_num
    q = deque([start])
    visited[start] = 0
    while q:
        current = q.popleft()
        for adj in adjs[current]:
        if visited[adj]>=0:continue
        q.append(adj)
        visited[adj] = visited[current] + 1
    
    return visited[end]