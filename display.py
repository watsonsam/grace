import pygame

pygame.init()


def draw_maze(maze, cell_size):
    screen = pygame.Surface([(maze.width * cell_size) + 1, (maze.height * cell_size) + 1])
    screen.fill((255, 255, 255))

    for k, v in maze.grid.items():
        x, y = k
        line_colour = (255, 100, 255)
        line_width = 3
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

    pygame.image.save(screen, "test.png")

    pygame.quit()
