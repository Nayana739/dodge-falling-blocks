import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player
player_width, player_height = 50, 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Enemy (falling blocks)
block_width, block_height = 50, 50
block_x = random.randint(0, WIDTH - block_width)
block_y = -block_height
block_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Move block
    block_y += block_speed
    if block_y > HEIGHT:
        block_y = -block_height
        block_x = random.randint(0, WIDTH - block_width)
        score += 1

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    block_rect = pygame.Rect(block_x, block_y, block_width, block_height)
    if player_rect.colliderect(block_rect):
        print("Game Over! Your score:", score)
        running = False

    # Draw player and block
    pygame.draw.rect(screen, BLACK, player_rect)
    pygame.draw.rect(screen, RED, block_rect)

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
