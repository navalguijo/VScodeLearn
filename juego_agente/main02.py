# el programa al arrancar abre una pantalla gráfica con 2 botones: el primer boton llamará a main.py y arrancará ese juego, el segundo cerrará la aplicación
import pygame
import sys
import os
# Inicializar pygame
pygame.init()
# Configuración de la ventana
WIDTH, HEIGHT = 640, 480
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Menú Principal')
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
# Fuente
font = pygame.font.SysFont(None, 40)
# Botones
button_width, button_height = 200, 50
play_button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 - button_height - 10, button_width, button_height)
exit_button_rect = pygame.Rect(WIDTH // 2 - button_width // 2, HEIGHT // 2 + 10, button_width, button_height)
# Bucle principal del menú
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    # Aquí se llamaría a main.py para iniciar el juego
                    import main
                    main.main()  # Llama a la función principal del juego
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
        # Dibujar el menú
        window.fill(WHITE)
        pygame.draw.rect(window, GRAY, play_button_rect)
        pygame.draw.rect(window, GRAY, exit_button_rect)
        play_text = font.render('Jugar', True, BLACK)
        exit_text = font.render('Salir', True, BLACK)
        window.blit(play_text, (play_button_rect.x + 50, play_button_rect.y + 10))
        window.blit(exit_text, (exit_button_rect.x + 50, exit_button_rect.y + 10))
        pygame.display.flip()  
if __name__ == "__main__":    main_menu()
