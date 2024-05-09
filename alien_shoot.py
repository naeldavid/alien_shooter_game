import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the game
pygame.display.set_caption("Alien Shooter")

# Load images
player_image = pygame.image.load("Assault_rifle_icon.png")
alien_image = pygame.image.load("alien.png")

# Set player position
player_x = screen_width / 2
player_y = screen_height - 100

# Set alien position
alien_x = random.randint(50, screen_width - 50)
alien_y = 50

# Set game loop
running = True

# Set score
score = 0

# Set font
font = pygame.font.SysFont("Arial", 30)

# Game loop
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Shoot bullet
                bullet_x = player_x + 25
                bullet_y = player_y - 10

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5

    # Move alien
    alien_y += 3

    # Collision detection
    if alien_y > screen_height:
        alien_x = random.randint(50, screen_width - 50)
        alien_y = 50
        score += 1
    if bullet_y < 0:
        bullet_x = 0
        bullet_y = 0
    if bullet_x > alien_x and bullet_x < alien_x + 50 and bullet_y < alien_y + 50:
        alien_x = random.randint(50, screen_width - 50)
        alien_y = 50
        score += 10
        bullet_x = 0
        bullet_y = 0

    # Draw images
    screen.blit(player_image, (player_x, player_y))
    screen.blit(alien_image, (alien_x, alien_y))

    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.update()

    # Set frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

# Quit Pygame
pygame.quit()
