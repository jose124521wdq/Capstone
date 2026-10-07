import pygame

pygame.init()

class Set():
    #Colors
    BLACK = (0, 0, 0)
    ORANGE = (220, 190, 0)
    DARK_ORANGE = (140, 110, 0)

    def __init__(self, x, y, size, color, bg):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.bg = bg

        
        self.layer = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.layer_rect = self.layer.get_rect()


        self.rect = pygame.Rect(0,0, self.size, self.size)
        self.rect.center = (self.x, self.y)
        
        self.nums = []



    def update(self, screen):
        self.layer.fill((0, 0, 0, 0))
        pygame.draw.circle(self.layer, self.color , self.layer_rect.center, self.size/2)

        screen.blit(self.layer, (self.x - self.size / 2, self.y- self.size / 2))
        
