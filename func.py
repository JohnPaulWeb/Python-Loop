import pygame.examples.aliens as aliens
aliens

import pygame
pygame.init()
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Basket properties
basket_width = 100
basket_height = 20
basket_x = (SCREEN_WIDTH - basket_width) // 2
basket_y = SCREEN_HEIGHT - basket_height - 10
basket_speed = 10

# Object properties
object_width = 20
object_height = 20
object_x = random.randint(0, SCREEN_WIDTH - object_width)
object_y = -object_height
object_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < SCREEN_WIDTH - basket_width:
        basket_x += basket_speed

    # Move the falling object
    object_y += object_speed

    # Check if the object hits the basket
    if (
        object_y + object_height > basket_y
        and basket_x < object_x < basket_x + basket_width
    ) or (
        object_y + object_height > basket_y
        and basket_x < object_x + object_width < basket_x + basket_width
    ):
        score += 1
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_y = -object_height

    # Reset object if it falls off screen
    if object_y > SCREEN_HEIGHT:
        object_x = random.randint(0, SCREEN_WIDTH - object_width)
        object_y = -object_height

    # Draw the basket
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # Draw the falling object
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
