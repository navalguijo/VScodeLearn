import pygame
import sys
import os

# Inicializar pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Juego Básico con Pygame')

# Colores
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 5

def load_dragon_frames(path, frame_w, frame_h, grid_w, grid_h, player_size):
    frames = []
    if os.path.exists(path):
        spritesheet = pygame.image.load(path).convert_alpha()
        for y in range(grid_h):
            for x in range(grid_w):
                rect = pygame.Rect(
                    int(x * frame_w),
                    int(y * frame_h),
                    int(frame_w),
                    int(frame_h)
                )
                frame = spritesheet.subsurface(rect)
                frame = pygame.transform.scale(frame, (player_size, player_size))
                frames.append(frame)
    return frames

dragon01_path = os.path.join('graficos', 'javi_dragon01.png')
dragon02_path = os.path.join('graficos', 'javi_dragon02.png')
dragon01_frames = load_dragon_frames(dragon01_path, 32, 32, 2, 2, player_size)
dragon02_frames = load_dragon_frames(dragon02_path, 512, 2048 // 6, 4, 6, player_size)
current_dragon_frames = dragon01_frames if dragon01_frames else None

# Bucle principal
def main():
    global player_x, player_y
    import random
    clock = pygame.time.Clock()
    running = True
    player_color = BLUE
    show_dragon = False
    dragon_anim_index = 0
    dragon_anim_timer = 0
    dragon_flip = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    player_color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                if event.key == pygame.K_t:
                    show_dragon = True
                    current_dragon_frames = dragon01_frames if dragon01_frames else None
                    dragon_anim_index = 0
                    dragon_anim_timer = 0
                if event.key == pygame.K_r:
                    show_dragon = True
                    current_dragon_frames = dragon02_frames if dragon02_frames else None
                    dragon_anim_index = 0
                    dragon_anim_timer = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player_x -= player_speed
            dragon_flip = False
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player_x += player_speed
            dragon_flip = True
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        player_x = max(0, min(WIDTH - player_size, player_x))
        player_y = max(0, min(HEIGHT - player_size, player_y))

        window.fill(RED)

        if show_dragon and current_dragon_frames:
            # Animación del dragón
            dragon_anim_timer += clock.get_time()
            num_frames = len(current_dragon_frames)
            if dragon_anim_timer > 120:
                dragon_anim_index = (dragon_anim_index + 1) % num_frames
                dragon_anim_timer = 0
            frame = current_dragon_frames[dragon_anim_index]
            if dragon_flip:
                frame = pygame.transform.flip(frame, True, False)
            window.blit(frame, (player_x, player_y))
        else:
            pygame.draw.rect(window, player_color, (player_x, player_y, player_size, player_size))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
