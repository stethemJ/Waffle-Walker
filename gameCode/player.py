import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../assets/WaffleCharacter.png").convert()
        self.rect = self.image.get_rect()