    from collections import deque

class SmartRouteAgent:

    def __init__(self, graph):
        self.graph = graph

    def bfs(self, start, goal):
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)

                for neighbor in self.graph[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

        return None

    def dfs(self, start, goal, path=[]):
        path = path + [start]

        if start == goal:
            return path

        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_path = self.dfs(neighbor, goal, path)
                if new_path:
                    return new_path

        return None


graph = {
    'Home': ['A'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

agent = SmartRouteAgent(graph)

print("BFS Path:", agent.bfs('Home', 'D'))
print("DFS Path:", agent.dfs('Home', 'D'))