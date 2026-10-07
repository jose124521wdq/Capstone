import pygame

pygame.init()

class Text():
    #Colors
    BLACK = (0, 0, 0)
    ORANGE = (220, 190, 0)
    DARK_ORANGE = (140, 110, 0)

    def __init__(self, x, y, width, height, size, color, bg, message, font_type=None):
        self.x = x
        self.y = y
        self.width = width
        self. height = height
        
        self.size = size
        self.color = color
        self.bg = bg
        self.message = message

        self.rect = pygame.Rect(x, y, width, height)
        self.shadow_rect = pygame.Rect(x,y, width, height)
                
        self.rect.center = (self.x,self.y)
        
        #Set font type and size
        self.font = pygame.font.SysFont(font_type, self.size)
        self.text = self.font.render(message, True, self.color)
        self.text_rect = self.text.get_rect()

        self.text_rect.center = self.rect.center


    def update(self, screen):
        self.rect.width = self.width
        self.rect.height = self.height

        self.rect.center = (self.x, self.y)
        
        self.shadow_rect.width = self.width
        self.shadow_rect.height = self.height

        self.shadow_rect.center = (self.x+11, self.y + 11)

        
        pygame.draw.rect(screen, (50,50,50), self.shadow_rect)
        pygame.draw.rect(screen, self.bg, self.rect)
        screen.blit(self.text, self.text_rect)
