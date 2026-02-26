import pygame
import sys
import math
import os

pygame.init()

WIDTH, HEIGHT = 900, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Galaxy Bario')

WHITE = (255, 255, 255)
PLANET_COLOR = (120, 120, 200)
PLATFORM_COLOR = (180, 180, 255)

# Lista de planetas
planets = [
    {'x': WIDTH // 2, 'y': HEIGHT // 2, 'radius': 180},
    {'x': WIDTH // 2 + 300, 'y': HEIGHT // 2 - 150, 'radius': 120},
    {'x': WIDTH // 2 - 250, 'y': HEIGHT // 2 + 200, 'radius': 100}
]

# Plataformas flotantes (ahora asociadas a planetas)
platforms = [
    {'planet': 0, 'angle': math.pi / 4, 'radius': planets[0]['radius'] + 100},
    {'planet': 0, 'angle': 3 * math.pi / 4, 'radius': planets[0]['radius'] + 120},
    {'planet': 1, 'angle': math.pi / 2, 'radius': planets[1]['radius'] + 60},
    {'planet': 2, 'angle': math.pi, 'radius': planets[2]['radius'] + 50}
]

# Estado del personaje
player_planet = 0
player_radius = planets[player_planet]['radius'] + 40
player_angle = math.pi / 2
player_speed = 0.045
jump_power = 16
velocity = 0
on_ground = True
spin_timer = 0
spin_duration = 20
player_facing_right = True

clock = pygame.time.Clock()
gravity = 0.7
running = True

player_size = 60
bario_sprite_path = os.path.join('graficos', 'bario.png')
bario_sprite = pygame.image.load(bario_sprite_path).convert_alpha()
bario_sprite = pygame.transform.scale(bario_sprite, (player_size, player_size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x and spin_timer == 0:
                spin_timer = spin_duration

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        player_angle -= player_speed
        player_facing_right = False
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        player_angle += player_speed
        player_facing_right = True
    if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]) and on_ground:
        velocity = -jump_power
        on_ground = False

    # Spin (giro)
    if spin_timer > 0:
        player_angle += 0.13 * (1 if player_facing_right else -1)
        spin_timer -= 1

    # Gravedad planetaria
    planet = planets[player_planet]
    prev_on_ground = on_ground
    on_ground = False
    if not prev_on_ground:
        velocity += gravity
        player_radius += velocity
    # Colisión con plataformas flotantes
    for plat in platforms:
        if plat['planet'] == player_planet:
            plat_x = planet['x'] + int(plat['radius'] * math.cos(plat['angle']))
            plat_y = planet['y'] + int(plat['radius'] * math.sin(plat['angle']))
            px = planet['x'] + int(player_radius * math.cos(player_angle))
            py = planet['y'] + int(player_radius * math.sin(player_angle))
            dist = math.hypot(px - plat_x, py - plat_y)
            if dist < player_size and abs(player_radius - plat['radius']) < 10 and velocity >= 0:
                player_radius = plat['radius']
                velocity = 0
                on_ground = True
    # Colisión con planeta
    if player_radius <= planet['radius'] + 40 and velocity >= 0:
        player_radius = planet['radius'] + 40
        velocity = 0
        on_ground = True
    # Cambio de planeta si salta lejos
    for idx, p in enumerate(planets):
        px = p['x'] + int(player_radius * math.cos(player_angle))
        py = p['y'] + int(player_radius * math.sin(player_angle))
        dist = math.hypot(px - p['x'], py - p['y'])
        if dist < p['radius'] + 60 and idx != player_planet:
            player_planet = idx
            planet = planets[player_planet]
            player_radius = planet['radius'] + 40
            velocity = 0
            on_ground = True
            break

    # Si cae fuera de pantalla, reaparece en planeta principal
    if player_radius > HEIGHT:
        player_planet = 0
        planet = planets[player_planet]
        player_radius = planet['radius'] + 40
        velocity = 0
        on_ground = True

    window.fill((40, 60, 120))  # Fondo tipo Galaxy
    # Dibujar planetas
    for p in planets:
        pygame.draw.circle(window, PLANET_COLOR, (p['x'], p['y']), p['radius'])
        pygame.draw.circle(window, (80, 80, 160), (p['x'], p['y']), p['radius'], 8)
    # Dibujar plataformas flotantes
    for plat in platforms:
        p = planets[plat['planet']]
        plat_x = p['x'] + int(plat['radius'] * math.cos(plat['angle']))
        plat_y = p['y'] + int(plat['radius'] * math.sin(plat['angle']))
        pygame.draw.rect(window, PLATFORM_COLOR, (plat_x - 30, plat_y - 10, 60, 20), border_radius=8)
    # Dibujar personaje
    planet = planets[player_planet]
    px = planet['x'] + int(player_radius * math.cos(player_angle))
    py = planet['y'] + int(player_radius * math.sin(player_angle))
    rotated_sprite = pygame.transform.rotate(bario_sprite, -math.degrees(player_angle) + 90)
    if not player_facing_right:
        rotated_sprite = pygame.transform.flip(rotated_sprite, True, False)
    rect = rotated_sprite.get_rect(center=(px, py))
    window.blit(rotated_sprite, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
