import heapq
from collections import defaultdict
from typing import Dict, List, Tuple, Optional, Any
from backend.database.controlers.places import get_place_by_id_controller

from backend.database.models import Neighbor


class Graph:
    def __init__(self, all_info_of_neighbors: List[Dict[str, Any]]):
        self.adj: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        for neighbor in all_info_of_neighbors:
            self.add_edge(**neighbor)

    def find_all_simple_paths(
            self,
            start: str,
            end: str,
            max_depth: Optional[int] = None,
    ) -> List[Dict[str, object]]:

        results = []

        def dfs(node, path, visited, distance):
            if max_depth is not None and len(path) > max_depth:
                return

            if node == end:
                results.append(path.copy())
                # results.append({
                #     "path": path.copy(),
                #     "distance": distance
                # })
                return

            for neighbor, weight in self.neighbors(node):
                if neighbor in visited:
                    continue

                visited.add(neighbor)
                path.append(neighbor)

                dfs(neighbor, path, visited, distance + weight)

                path.pop()
                visited.remove(neighbor)

        dfs(
            node=start,
            path=[],
            visited={start},
            distance=0
        )

        return results

    def add_edge(
        self,
        first_node: str,
        second_node: str,
        distance: int = 1,
        bidirectional: bool = True,
        **kwargs,
    ):
        self.adj[first_node].append((second_node, distance))
        if bidirectional:
            self.adj[second_node].append((first_node, distance))

    def neighbors(self, node: str):
        return self.adj.get(node, [])

    # 🔥 Dijkstra implementation
    def dijkstra(self, start: str, goal: str) -> Optional[Dict[int, List[str]]]:
        """
        Returns:
            (total_distance, path) or None if unreachable
        """

        # Priority queue: (distance_so_far, node)
        pq = [(0, start)]

        # Best known distances
        distances: Dict[str, int] = {start: 0}

        # To reconstruct path
        previous: Dict[str, Optional[str]] = {start: None}

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            # Stop early if we reached the goal
            if current_node == goal:
                break

            # Skip outdated queue entries
            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.neighbors(current_node):
                new_dist = current_dist + weight

                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))

        # Goal unreachable
        if goal not in distances:
            {"distance":None, "path":None}

        # Reconstruct path
        path = []
        node = goal
        while node is not None:
            path.append(node)
            node = previous[node]
        path.reverse()


        # place_in_detail = []
        # for _path_id in path:
        #     place = get_place_by_id_controller(_path_id)
        #     place_in_detail.append(place)

        return {"distance":distances[goal], "path":path}
