import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 900, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galaxy Bario')

WHITE = (255, 255, 255)
BLUE = (0, 102, 255)
BLACK = (0, 0, 0)
PLANET_COLOR = (120, 120, 200)

planet_x = WIDTH // 2
planet_y = HEIGHT // 2
planet_radius = 180

def draw_planet():
    pygame.draw.circle(window, PLANET_COLOR, (planet_x, planet_y), planet_radius)
    pygame.draw.circle(window, (80, 80, 160), (planet_x, planet_y), planet_radius, 8)

# Bario: igual a Mario, azul, sin cara, gorra con B
player_radius = planet_radius + 40
player_angle = math.pi / 2  # Empieza arriba
player_speed = 0.04
jump_power = 16
velocity = 0
on_ground = True

def draw_bario(angle, r):
    # Posición polar a cartesiana
    x = planet_x + int(r * math.cos(angle))
    y = planet_y + int(r * math.sin(angle))
    # Cuerpo
    pygame.draw.rect(window, BLUE, (x - 20, y - 40, 40, 60))
    # Gorra azul
    pygame.draw.rect(window, (0, 70, 200), (x - 20, y - 55, 40, 15))
    # Letra B en la gorra
    font = pygame.font.SysFont('Arial', 18, bold=True)
    text = font.render('B', True, WHITE)
    window.blit(text, (x - 5, y - 53))
    # No hay cara

clock = pygame.time.Clock()
running = True
gravity = 0.7

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        player_angle -= player_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        player_angle += player_speed
    if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and on_ground:
        velocity = -jump_power
        on_ground = False

    # Gravedad planetaria
    if not on_ground:
        velocity += gravity
        player_radius += velocity
        if player_radius >= planet_radius + 40:
            player_radius = planet_radius + 40
            velocity = 0
            on_ground = True

    window.fill(WHITE)
    draw_planet()
    draw_bario(player_angle, player_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
