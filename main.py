import maze
import display
from timeit import default_timer as timer


def main():
    start = timer()
    width = 3
    height = 3
    grid, graph = maze.build(width, height)
    maze_time = timer()
    print("Took " + str(maze_time - start) + " to build the maze")
    print(grid)
    print(graph)
    display.draw_maze(grid, 10, "test_again.png")
    # start = timer()
    # display.draw_maze(the_maze, 10, "test.png", True, (0, 0), ((width - 1), (height - 1)))
    # # display.draw_maze(the_maze, 10, "test.png", True, (10, 10), (10, 20))
    # stop = timer()
    # print("Took " + str(stop - start) + " to draw the maze")

if __name__ == '__main__':
    main()