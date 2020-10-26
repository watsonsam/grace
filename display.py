import pygame

pygame.init()


def draw_maze(maze, cell_size):
    screen = pygame.Surface([(maze.width * cell_size) + 1, (maze.height * cell_size) + 1])
    screen.fill((255, 255, 255))

    for k, v in maze.grid.items():
        x, y = k
        line_colour = (255, 100, 255)
        if v.north:
            pygame.draw.line(screen, line_colour, (x * cell_size, y * cell_size),
                             ((x * cell_size) + cell_size, y * cell_size), 3)
        if v.south:
            pygame.draw.line(screen, line_colour, (x * cell_size, (y * cell_size) + cell_size),
                             ((x * cell_size) + cell_size, (y * cell_size) + cell_size), 3)
        if v.east:
            pygame.draw.line(screen, line_colour, ((x * cell_size) + cell_size, y * cell_size),
                             ((x * cell_size) + cell_size, (y * cell_size) + cell_size), 3)
        if v.west:
            pygame.draw.line(screen, line_colour, (x * cell_size, y * cell_size),
                             (x * cell_size, (y * cell_size) + cell_size), 3)

    pygame.image.save(screen, "test.png")

    pygame.quit()
