import cell
import random


# TODO: Get rid of class
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = {}
        self.build_grid()
        self.build_maze()

    def build_grid(self):
        for w in range(self.width):
            for h in range(self.height):
                self.grid[(w, h)] = cell.Cell()

    def get_neighbours(self, x_y):
        x, y = x_y
        neighbours = []
        # north nbr
        if y > 0:
            neighbours.append((x, y - 1))
        # south nbr
        if y < (self.height - 1):
            neighbours.append((x, y + 1))
        # east nbr
        if x < (self.width - 1):
            neighbours.append((x + 1, y))
        # west nbr
        if x > 0:
            neighbours.append((x - 1, y))

        return neighbours

    def join_cells(self, x1_y1, x2_y2):
        x1, y1 = x1_y1
        x2, y2 = x2_y2
        cell1 = self.grid[(x1, y1)]
        cell2 = self.grid[(x2, y2)]
        # check that the cells are neighbours
        if (x1, y1) in self.get_neighbours((x2, y2)):
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

    def get_unvisited_neighbours(self, x_y):
        unvisited_neighbours = []
        neighbours = self.get_neighbours(x_y)
        for nbr in neighbours:
            if not self.grid[nbr].visited:
                unvisited_neighbours.append(nbr)
        return unvisited_neighbours

    def build_maze(self):
        start_x = random.randint(0, self.width - 1)
        start_y = random.randint(0, self.height - 1)
        self.build((start_x, start_y))

    # TODO: make non-recursive
    def build(self, x_y):
        nodes_to_visit = [x_y]

        while len(nodes_to_visit) > 0:
            node = nodes_to_visit[-1]
            #print(node)
            if not self.grid[node].visited:
                self.grid[node].visited = True
            unvisited_neighbours = self.get_unvisited_neighbours(node)
            if len(unvisited_neighbours) > 0:
                next_node = random.choice(unvisited_neighbours)
                self.join_cells(node, next_node)
                nodes_to_visit.append(next_node) #leaving previous node to come back to
            else:
                nodes_to_visit.remove(node)

