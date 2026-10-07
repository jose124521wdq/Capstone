import pygame
import number

pygame.init()

class Ellipse():
    #Colors
    BLACK = (0, 0, 0)
    ORANGE = (220, 190, 0)
    DARK_ORANGE = (140, 110, 0)

    def __init__(self, x, y, width, height, color, nums=[1,2,3]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rect = pygame.Rect(0,0, width, height)
        self.rect.center = (self.x, self.y)
        self.rect_shadow = pygame.Rect(0,0,width,height)
        self.rect_shadow.center = (self.x+12, self.y+12)
        self.rect_shadow2 = pygame.Rect(0,0, width, height)
        self.rect_shadow2.center = (self.x+20, self.y+20)


        self.nums_list = nums
        self.quantity = len(nums)
        self.num_cards = self.get_num_cards(self.nums_list)



    def get_num_cards(self, nums):
        start_y = self.y
        end_y = self.y + self.height
        num_cards = []
        distance = self.height / (self.quantity + 1)
        for i in range(self.quantity):
            num_card = number.Number(self.x, (self.y - self.height/2)+(distance * (i+1)), nums[i])

            num_cards.append(num_card)
        return num_cards


            



    def update(self, screen):
        pygame.draw.ellipse(screen, (30,30,30) , self.rect_shadow2)
        pygame.draw.ellipse(screen, (10,10,10) , self.rect_shadow)
        pygame.draw.ellipse(screen, self.color , self.rect)
        pygame.draw.ellipse(screen, (40,40,40) , self.rect, 6)

        for card in self.num_cards:
            card.update(screen)


