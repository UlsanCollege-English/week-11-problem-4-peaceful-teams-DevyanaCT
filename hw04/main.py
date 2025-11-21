from collections import deque

def bipartition(graph):
    """Return (left_set, right_set) if bipartite; else None.

    Uses BFS coloring over all components.
    color[node] = 0 or 1.
    If same-color neighbors appear → return None.
    """

    color = {}

    for start in graph:
        if start not in color:
            # Start BFS for this component
            color[start] = 0
            q = deque([start])

            while q:
                u = q.popleft()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]   # opposite color
                        q.append(v)
                    else:
                        # If neighbor has same color → not bipartite
                        if color[v] == color[u]:
                            return None

    # Build the two sets
    left = {node for node, c in color.items() if c == 0}
    right = {node for node, c in color.items() if c == 1}

    return (left, right)
