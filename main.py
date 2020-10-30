import maze
import display
from timeit import default_timer as timer


def main():
    start = timer()
    width = 1000 #200
    height = 1000 #200
    the_maze = maze.Maze(width, height)
    maze_time = timer()
    # print("Took " + str(maze_time - start) + " to build the maze")
    start = timer()
    display.draw_maze(the_maze, 10, "test.png", True, (0, 0), ((width - 1), (height - 1)))
    stop = timer()
    # print("Took " + str(stop - start) + " to draw the maze")

if __name__ == '__main__':
    main()