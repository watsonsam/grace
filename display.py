import pygame

pygame.init()


def draw_maze(maze, cell_size, file_name, with_solution=False, sol_start=(0, 0), sol_end=(0, 0)):
    screen = pygame.Surface([(maze.width * cell_size) + 1, (maze.height * cell_size) + 1])
    screen.fill((255, 255, 255))

    for k, v in maze.grid.items():
        x, y = k
        # line_colour = (255, 100, 255)
        line_colour = (0, 0, 0)
        line_width = 1
        if v.north:
            pygame.draw.aaline(screen, line_colour, (x * cell_size, y * cell_size),
                               ((x * cell_size) + cell_size, y * cell_size), line_width)
        if v.south:
            pygame.draw.aaline(screen, line_colour, (x * cell_size, (y * cell_size) + cell_size),
                               ((x * cell_size) + cell_size, (y * cell_size) + cell_size), line_width)
        if v.east:
            pygame.draw.aaline(screen, line_colour, ((x * cell_size) + cell_size, y * cell_size),
                               ((x * cell_size) + cell_size, (y * cell_size) + cell_size), line_width)
        if v.west:
            pygame.draw.aaline(screen, line_colour, (x * cell_size, y * cell_size),
                               (x * cell_size, (y * cell_size) + cell_size), line_width)

    if with_solution:
        draw_solution(screen, maze, cell_size, sol_start, sol_end)
    pygame.image.save(screen, file_name)

    pygame.quit()


def draw_solution(screen, maze, cell_size, start, end):
    solution = maze.solve(start, end)
    print(solution)
    centre = cell_size / 2
    while len(solution) > 1:
        x, y = solution.pop(0)
        x1, y1 = solution[0]
        pygame.draw.aaline(screen, (255, 0, 0), ((x * cell_size) + centre, ((y * cell_size) + centre)),
                           ((x1 * cell_size) + centre, ((y1 * cell_size) + centre)))
