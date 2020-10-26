import pygame
pygame.init()


def draw_maze(maze, cell_size):
    running = True
    screen = pygame.display.set_mode([(maze.width * cell_size) + 1, (maze.height * cell_size) + 1])
    screen.fill((255, 255, 255))

    for k, v in maze.grid.items():
        x, y = k
        if v.north:
            pygame.draw.line(screen, (0, 0, 0), (x * cell_size, y * cell_size),
                             ((x * cell_size) + cell_size, y * cell_size), 3)
        if v.south:
            pygame.draw.line(screen, (0, 0, 0), (x * cell_size, (y * cell_size) + cell_size),
                             ((x * cell_size) + cell_size, (y * cell_size) + cell_size), 3)
        if v.east:
            pygame.draw.line(screen, (0, 0, 0), ((x * cell_size) + cell_size, y * cell_size),
                             ((x * cell_size) + cell_size, (y * cell_size) + cell_size), 3)
        if v.west:
            pygame.draw.line(screen, (0, 0, 0), (x * cell_size, y * cell_size),
                             (x * cell_size, (y * cell_size) + cell_size), 3)

    pygame.display.flip()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


    pygame.quit()