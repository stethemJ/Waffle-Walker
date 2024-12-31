import pygame
from background import Background
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((1792,1024))
    clock = pygame.time.Clock()
    running = True
    dt = .01
    
    bg = Background()
    
    player = Player()  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 0  # go to y

    player_list = pygame.sprite.Group()
    player_list.add(player)

    while running:
        screen.fill((0, 0, 0))
        screen.blit(bg.MainBackground, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        player_list.draw(screen)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.rect.y -= 300 * dt
        if keys[pygame.K_s]:
            player.rect.y += 300 * dt
        if keys[pygame.K_a]:
            player.rect.x -= 300 * dt
        if keys[pygame.K_d]:
            player.rect.x += 300 * dt
        pygame.display.flip()
    
if __name__ == "__main__":
    main()