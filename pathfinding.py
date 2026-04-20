from collections import deque


class PathFinding:
    def __init__(self, game):
        self.game = game
        self.ways = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]

    def get_path(self, start, goal):
        if start == goal:
            return start
        visited = self.bfs(start, goal)
        if goal not in visited:
            return start
        path = [goal]
        step = visited[goal]
        while step and step != start:
            path.append(step)
            step = visited[step]
        return path[-1] if path else start

    def bfs(self, start, goal):
        queue = deque([start])
        visited = {start: None}
        max_nodes = 5000

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break
            for next_node in self.get_next_nodes(cur_node):
                if next_node in visited or next_node in self.game.object_handler.npc_positions:
                    continue
                visited[next_node] = cur_node
                queue.append(next_node)
                if len(visited) >= max_nodes:
                    return visited
        return visited

    def get_next_nodes(self, position):
        x, y = position
        return [
            (x + dx, y + dy)
            for dx, dy in self.ways
            if not self.game.map.is_wall(x + dx, y + dy)
        ]
