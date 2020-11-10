import random


# from timeit import default_timer as timer


class Cell:

    def __init__(self):
        self.north = True
        self.south = True
        self.east = True
        self.west = True
        self.visited = False


def build(width: int, height: int) -> (dict, dict):
    the_maze = _build_maze(width, height)
    return the_maze


def _build_maze(width, height):
    def _get_neighbours(x_y):
        x, y = x_y
        neighbours = []
        # north nbr
        if y > 0:
            neighbours.append((x, y - 1))
        # south nbr
        if y < (height - 1):
            neighbours.append((x, y + 1))
        # east nbr
        if x < (width - 1):
            neighbours.append((x + 1, y))
        # west nbr
        if x > 0:
            neighbours.append((x - 1, y))

        return neighbours

    def _join_cells(x1_y1, x2_y2):
        x1, y1 = x1_y1
        x2, y2 = x2_y2
        if x1_y1 in graph.keys():
            graph[x1_y1].append(x2_y2)
        else:
            graph[x1_y1] = [x2_y2]
        if x2_y2 in graph.keys():
            graph[x2_y2].append(x1_y1)
        else:
            graph[x2_y2] = [x1_y1]
        cell1 = grid[(x1, y1)]
        cell2 = grid[(x2, y2)]
        if (x1, y1) in _get_neighbours((x2, y2)):
            if x1 < x2:
                cell1.east = False
                cell2.west = False
            elif y1 < y2:
                cell1.south = False
                cell2.north = False
            elif x2 < x1:
                cell1.west = False
                cell2.east = False
            elif y2 < y1:
                cell1.north = False
                cell2.south = False

    def _get_unvisited_neighbours(x_y) -> list:
        _unvisited_neighbours = []
        neighbours = _get_neighbours(x_y)
        for nbr in neighbours:
            if not grid[nbr].visited:
                _unvisited_neighbours.append(nbr)
        return _unvisited_neighbours

    grid = {}
    graph = {}

    for w in range(width):
        for h in range(height):
            grid[(w, h)] = Cell()
    start_x = random.randint(0, width - 1)
    start_y = random.randint(0, height - 1)
    nodes_to_visit = [(start_x, start_y)]

    while len(nodes_to_visit) > 0:
        node = nodes_to_visit[-1]
        if not grid[node].visited:
            grid[node].visited = True
        unvisited_neighbours = _get_unvisited_neighbours(node)
        if len(unvisited_neighbours) > 0:
            next_node = random.choice(unvisited_neighbours)
            _join_cells(node, next_node)
            nodes_to_visit.append(next_node)  # leaving previous node to come back to
        else:
            nodes_to_visit.remove(node)
    dim = (width, height)
    return {"dim": dim, "grid": grid}, {"dim": dim, "graph": graph}










# simple approach, not shortest path
# def solve(self, start, end):
#     start_time = timer()
#     nodes_to_visit = [start]
#     path = [start]
#     decision_point = [start]
#     visited = set(start)
#     deepest_path = 0
#     greatest_number_decisions = 0
#
#     while len(nodes_to_visit) > 0:
#         node = nodes_to_visit[-1]
#         path.append(node)
#         if len(path) > deepest_path:
#             deepest_path = len(path)
#         if len(decision_point) > greatest_number_decisions:
#             greatest_number_decisions = len(decision_point)
#         visited.add(node)
#
#         if node == end:
#             stop_time = timer()
#             print("Solution took ", str(stop_time - start_time), " seconds.")
#             print("Solution path length: ", len(path))
#             print("Deepest path length: ", deepest_path)
#             print("Greatest number of decisions: ", greatest_number_decisions)
#             return path
#         else:
#             unvisited = [n for n in graph[node] if n not in visited]
#             if len(unvisited) > 0:
#                 if len(unvisited) > 1:  # there's more than one option
#                     random.shuffle(unvisited)
#                     decision_point.append(unvisited[0])
#                     nodes_to_visit.append(unvisited[0])
#                 else:
#                     nodes_to_visit.append(unvisited[0])
#             else:
#                 # print("visited: ", visited)
#                 # print("nodes to visit: ", nodes_to_visit)
#                 # print("dps: ", decision_point)
#                 # print("path: ", path)
#                 dp = decision_point.pop()
#                 nodes_to_visit = nodes_to_visit[0: nodes_to_visit.index(dp)]
#                 path = path[0: path.index(dp)]
#
#     return []
