import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Juego Básico con Pygame')

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Jugador
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5

# Bucle principal
def main():
    global player_x, player_y
    import random
    clock = pygame.time.Clock()
    running = True
    player_color = BLUE
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    # Cambia a un color aleatorio
                    player_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # Limitar el movimiento dentro de la ventana
        player_x = max(0, min(WIDTH - player_size, player_x))
        player_y = max(0, min(HEIGHT - player_size, player_y))

        window.fill(WHITE)
        pygame.draw.rect(window, player_color, (player_x, player_y, player_size, player_size))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
