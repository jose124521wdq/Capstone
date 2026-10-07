import pygame

pygame.init()

class Number():
    def __init__(self, x, y, number, bg=(255,255,255), color=(0,0,0), font_type=None):
        self.x = x
        self.y = y
        self.size = 60
        self.color = color
        self.bg = bg
        self.number = number
        self.font_type = font_type

        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.rect.center = (x, y)


        self.font = pygame.font.SysFont(font_type, self.size)
        self.text = self.font.render(str(number), True, self.color)
        self.text_rect = self.text.get_rect()

        self.text_rect.center = self.rect.center
        
    def update(self, screen):
        pygame.draw.rect(screen, self.bg, self.rect, border_radius=15)
        pygame.draw.rect(screen, (10,10,10), self.rect, width=5, border_radius=15)
        
        self.text_rect.center = self.rect.center
        screen.blit(self.text, self.text_rect)

    def get_pos(self):
        return (self.x, self.y)
