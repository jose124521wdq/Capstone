import pygame

pygame.init()

class Button():
    #Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ORANGE = (220, 190, 0)
    DARK_ORANGE = (140, 110, 0)

    

    
    def __init__(self, x, y, width, height, message):
        self.bg = ()
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.message = message

        self.rect = pygame.Rect(x, y, width, height)
        self.shadow_rect = pygame.Rect(x+10, y+10, width, height)

        
        self.font = pygame.font.SysFont(None, 35)
        self.text = self.font.render(message, True, self.BLACK)
        self.text_rect = self.text.get_rect()
        
        self.text_rect.center = self.rect.center

        self.is_hovering = False;

    def update(self,screen, mouse_pos):
        self.hovering(mouse_pos)
        
        if self.is_hovering:
            self.rect = pygame.Rect(self.x-10, self.y-10, self.width+20, self.height+10)
            self.shadow_rect = pygame.Rect(self.x, self.y, self.width+20, self.height+10)
            self.text_rect.center = self.rect.center

            
            pygame.draw.rect(screen, self.BLACK, self.shadow_rect)
            pygame.draw.rect(screen, self.WHITE, self.rect)
            screen.blit(self.text, self.text_rect)

        else:
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.shadow_rect = pygame.Rect(self.x+10, self.y+10, self.width, self.height)
            self.text_rect.center = self.rect.center
            
            pygame.draw.rect(screen, self.BLACK, self.shadow_rect)
            pygame.draw.rect(screen, self.ORANGE, self.rect)
            screen.blit(self.text, self.text_rect)


    def hovering(self, mouse_pos):
        self.is_hovering= self.rect.collidepoint(mouse_pos)
        
