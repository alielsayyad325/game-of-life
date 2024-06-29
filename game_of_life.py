import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 10

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

# Function to initialize the grid randomly
def initialize_grid():
    return np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.9, 0.1])

# Function to update the grid according to the rules of the game
def update_grid(grid):
    new_grid = grid.copy()
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            neighbors = np.sum(grid[max(i-1, 0):min(i+2, GRID_WIDTH), max(j-1, 0):min(j+2, GRID_HEIGHT)]) - grid[i, j]
            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1
    return new_grid

# Function to draw the grid on the screen
def draw_grid(grid):
    screen.fill(BLACK)
    for i in range(GRID_WIDTH):
        for j in range(GRID_HEIGHT):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, WHITE, (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Main function to run the simulation
def main():
    grid = initialize_grid()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)
        draw_grid(grid)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
