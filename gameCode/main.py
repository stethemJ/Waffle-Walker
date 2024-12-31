import pygame
from background import Background

def main():
    pygame.init()
    screen = pygame.display.set_mode((1792,1024))
    clock = pygame.time.Clock()
    running = True
    
    bg = Background()
    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg.MainBackground, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        pygame.display.flip()
    
if __name__ == "__main__":
    main()