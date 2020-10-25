import cell


class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = {}
        self.build_grid()

    def build_grid(self):
        for w in range(self.width):
            for h in range(self.height):
                self.grid[(w, h)] = cell.Cell()

    def get_neighbours(self, x, y):
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

    def join_cells(self, (x1, y1), (x2, y2)):
        cell1 = self.grid[(x1, y1)]
        cell2 = self.grid[(x2, y2)]
        # check that the cells are neighbours
        if (x1, y1) in self.get_neighbours(x2, y2):
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

