import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up game constants
GRID_SIZE = 30
CELL_SIZE = 20
WIDTH, HEIGHT = GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(5, 5), (5, 6), (5, 7)]  # Initial snake body
        self.direction = (1, 0)  # Initial direction (right)

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, WHITE, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)

    def check_collision(self):
        head = self.body[0]

        # Wrap around to the opposite side if out of bounds
        if head[0] < 0:
            head = (GRID_SIZE - 1, head[1])
        elif head[0] >= GRID_SIZE:
            head = (0, head[1])
        elif head[1] < 0:
            head = (head[0], GRID_SIZE - 1)
        elif head[1] >= GRID_SIZE:
            head = (head[0], 0)

        # Check for collisions with itself
        if head in self.body[1:]:
            return True

        # Update the head position
        self.body[0] = head

        return False

# Define the Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn_food()

    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    def spawn_food(self):
        self.position = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

# Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Create instances of the Snake and Food classes
snake = Snake()
food = Food()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.direction != (0, 1):  # "W" key for up
                snake.direction = (0, -1)  # Move up
            elif event.key == pygame.K_s and snake.direction != (0, -1):  # "S" key for down
                snake.direction = (0, 1)  # Move down
            elif event.key == pygame.K_a and snake.direction != (1, 0):  # "A" key for left
                snake.direction = (-1, 0)  # Move left
            elif event.key == pygame.K_d and snake.direction != (-1, 0):  # "D" key for right
                snake.direction = (1, 0)  # Move right

    # Update the game state
    snake.move()

    # Check for collisions
    if snake.check_collision():
        running = False

    # Check if the snake eats the food
    if snake.body[0] == food.position:
        food.spawn_food()
    else:
        snake.body.pop()

    # Draw game elements
    screen.fill((0, 0, 0))  # Fill the screen with black
    snake.draw()
    food.draw()

    pygame.display.flip()

    # Control the game speed
    clock.tick(7)  # Adjust this value to control the snake's speed

pygame.quit()
sys.exit()
