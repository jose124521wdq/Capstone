import pygame

pygame.init()

class Card():
    def __init__(self, x, y, number, font_type=None):
        self.x = x
        self.y = y
        self.size = 60
        self.color = (0,0,0)
        self.bg = (255,255,255)
        self.number = number
        self.font_type = font_type

        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.rect.center = (x, y)

        self.font = pygame.font.SysFont(font_type, self.size)
        self.text = self.font.render(str(number), True, self.color)
        self.text_rect = self.text.get_rect()

        self.text_rect.center = self.rect.center
        self.dragging = 0
        
    def update(self, screen):
        pygame.draw.rect(screen, self.bg, self.rect, border_radius=15)
        pygame.draw.rect(screen, (10,10,10), self.rect, width=5, border_radius=15)
        
        self.text_rect.center = self.rect.center
        screen.blit(self.text, self.text_rect)


class Card2():
    def __init__(self, x, y,width, height, size, number,color, bg, font_type=None):
        self.initial_x = x
        self.initial_y = y
        
        self.x = x
        self.y = y
        self.size = size
        self.width = width
        self.height = height
        
        self.color = color
        self.bg = bg
        self.number = number
        self.font_type = font_type

        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.center = (x, y)

        self.shadow_rect = pygame.Rect(x,y, self.width, self.height)


        self.font = pygame.font.SysFont(font_type, self.size)
        self.text = self.font.render(str(number), True, self.color)
        self.text_rect = self.text.get_rect()

        self.text_rect.center = self.rect.center
        self.dragging = 0

        self.locked = False
        self.space_using = None
        
    def update(self, screen):
        self.rect.center = (self.x, self.y)
        self.shadow_rect.center = (self.x+10, self.y+10)

        if self.locked:
            pygame.draw.rect(screen, self.bg, self.rect)

        else:
            pygame.draw.rect(screen,(40,40,40),self.shadow_rect)        
            pygame.draw.rect(screen, self.bg, self.rect)

        
        self.text_rect.center = self.rect.center
        screen.blit(self.text, self.text_rect)
