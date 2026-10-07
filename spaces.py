import pygame

pygame.init()

class Space():
    #Colors
    BLACK = (0, 0, 0)
    ORANGE = (220, 190, 0)
    DARK_ORANGE = (140, 110, 0)

    def __init__(self, x, y, width, height, bg,):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        self.bg = bg

        self.rect = pygame.Rect(x, y, width, height)
        self.rect.center = (x, y)

        self.shadow_rect = pygame.Rect(x,y, width, height)

        self.full = False
        self.shadow = True

        self.number = 0




    def update(self, screen):
        self.rect.center = (self.x,self.y)
        self.shadow_rect.center = (self.x+14, self.y + 14)

        pygame.draw.rect(screen, (40,40,40), self.shadow_rect, border_radius = 6)
        pygame.draw.rect(screen, self.bg, self.rect, border_radius = 6)




        

        
