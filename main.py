import maze
import display


def main():
    for i in range(3):
        the_maze = maze.Maze(30, 50)
        display.draw_maze(the_maze, 30)
        print("***************")

if __name__ == '__main__':
    main()