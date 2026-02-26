import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bario - Parodia de Mario')

WHITE = (255, 255, 255)
BLUE = (0, 102, 255)
BLACK = (0, 0, 0)
PLATFORM_COLOR = (100, 100, 100)

player_width = 40
player_height = 60
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 100
player_speed = 5
player_jump = 12
velocity_y = 0
on_ground = False

def draw_player(x, y):
    # Bario: cuerpo azul, sin cara
    pygame.draw.rect(window, BLUE, (x, y, player_width, player_height))
    # Gorra azul
    pygame.draw.rect(window, (0, 70, 200), (x, y, player_width, 15))

platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(200, 450, 200, 20),
    pygame.Rect(500, 350, 150, 20),
    pygame.Rect(100, 250, 120, 20)
]

gravity = 0.7
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed
    if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and on_ground:
        velocity_y = -player_jump
        on_ground = False

    velocity_y += gravity
    player_y += velocity_y

    # Colisión con plataformas
    on_ground = False
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for plat in platforms:
        if player_rect.colliderect(plat) and velocity_y >= 0:
            player_y = plat.top - player_height
            velocity_y = 0
            on_ground = True

    # Límites de pantalla
    player_x = max(0, min(WIDTH - player_width, player_x))
    if player_y > HEIGHT:
        player_y = HEIGHT - player_height - 100
        velocity_y = 0

    window.fill(WHITE)
    for plat in platforms:
        pygame.draw.rect(window, PLATFORM_COLOR, plat)
    draw_player(player_x, player_y)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
