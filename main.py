import maze
import display


def main():
    the_maze = maze.Maze(32, 50)
    display.draw_maze(the_maze, 20)

if __name__ == '__main__':
    main()