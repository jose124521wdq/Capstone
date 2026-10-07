import pygame
import sys
import os
import button
import text
import sets
import cards_set
import ellipse
import number
import spaces

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (220, 190, 0)
DARK_ORANGE = (140, 110, 0)
GREY = (10,10,10)
CLEAR_GREY = (40,40,40)

PUZZLE1 = (180,80,80); #(160,60,60)
PUZZLE2 = (50,150,250);


SET1 = (255,255,255, 230) #0,150,205,
SET2 = (250,220,0, 230) #220,190,0, 210



#FONT
font = pygame.font.SysFont(None, 35)

#PANTALLA
WIDTH = 1300
HEIGHT = 850
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Y_MID = HEIGHT / 2
X_MID = WIDTH / 2

score = 0

puzzle1_solved = False
puzzle2_solved = False
puzzle3_solved = False
puzzle4_solved = False


left_button = button.Button(WIDTH/11 *1 - 30, HEIGHT / 2, 80, 50, "<--")
right_button = button.Button(WIDTH/11 *10 - 30, HEIGHT / 2, 80, 50, "-->")

back_button = button.Button(X_MID - 200, 20, 400, 30, "REGRESAR")


def fade(width, height): 
    fade = pygame.Surface((width, height))
    fade.fill((4,4,4))
    for alpha in range(-60, 220):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def is_even(num):
    if num % 2 == 0:
        return True

def is_prime(num):
    num_divisors = 0
    if num <= 1:
        return False
    else:
        for i in range(num):
            if num % (i+1) == 0:
                num_divisors += 1

    if num_divisors == 2:
        return True
    else:
        return False

def is_puzzle1_solved(cards, set1_even, set2_prime):
    is_set1_valid = True
    is_set2_valid = True
    num_items_set1 = len(set1_even)
    num_items_set2 = len(set2_prime)
    num_items_shared = 0
    num_items_to_share = 0

    num_items = len(cards)

    
    for num in cards:
        if is_even(num) and is_prime(num):
            num_items_to_share += 1

    for item in set1_even:
        if item in set2_prime :
            num_items_shared += 1
    
    for item in set1_even:
        if not (is_even(item)):
            is_set1_valid = False

    for item in set2_prime:
        if not (is_prime(item)):
            is_set2_valid = False


    items_used = num_items_set1 + num_items_set2 - num_items_shared
    
    if is_set1_valid and is_set2_valid and items_used == num_items and (num_items_shared == num_items_to_share):
        return True

def is_puzzle2_solved(set1, set2, relations):
    set1_numbers = set1.nums_list
    set2_numbers = set2.nums_list

    total_pairs = 0

    valid_pairs = True
    num_relations = len(relations)

    for set1_number in set1_numbers:
        for set2_number in set2_numbers:
            if (is_divisible(set2_number, set1_number)):
                total_pairs += 1


    for relation in relations:
        divisor = relation[1]
        dividend = relation[0]

        if not(is_divisible(divisor, dividend)):
            valid_pairs = False

    if valid_pairs and num_relations == total_pairs:
        return True
        


def is_divisible(divisor,dividend):
    if divisor % dividend == 0:
        return True
    else:
        return False

def is_puzzle3_solved(domain_set, answers):
    range_set = []

    solved = True

    for num in domain_set:
        y = function(num)
        range_set.append(y)
        
    for i in range(len(range_set)):
        if range_set[i] != int(answers[i]):
            solved = False
            break
    if solved:
        return True
        
        

def function(x):
    return 2*(x) + 1
    
    
    



def main_menu():
    title = text.Text(X_MID, Y_MID - 280, WIDTH , 0, 160, (120,120,120), WHITE, "S C A P E  R O O M", "legal") #"courier"
    deco1 = text.Text(X_MID, HEIGHT/2, WIDTH , HEIGHT/2, 20, (120,120,120), WHITE, "") #"courier"

    
    shadow = text.Text(X_MID+5, Y_MID - 270, WIDTH , 0, 160, WHITE, GREY, "S C A P E  R O O M", "legal")
    play_button = button.Button(WIDTH/4,HEIGHT/2 - 25, WIDTH/2,50, "P L A Y")
    exit_button = button.Button(WIDTH/4,HEIGHT/1.5 - 25, WIDTH/2,50, "E X I T")


    black_door = pygame.image.load("black_door_menu.png").convert_alpha()
    black_door = pygame.transform.scale(black_door, (230,440))
    black_door_rect = black_door.get_rect()
    black_door_rect.center = (X_MID, Y_MID + 8)



    while True:
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if black_door_rect.collidepoint(event.pos):
                        black_door_rect.width = 50
                        black_door_rect.height = 100

                        
                        for i in range(1000):
                            black_door_rect.width +=  2.2
                            black_door_rect.height +=  4
                            black_door_rect.center = (X_MID, Y_MID)
                            pygame.draw.rect(screen, GREY, black_door_rect)
                            pygame.time.delay(1)
                            pygame.display.flip()
                        wall1()
                    
                    #if play_button.rect.collidepoint(event.pos):
                    #   fade(WIDTH, HEIGHT)
                    #   wall1()

                    #if exit_button.rect.collidepoint(event.pos):
                    #    pygame.quit()
                    #    sys.exit()

        screen.fill(GREY)

        deco1.update(screen)
        screen.blit(black_door, black_door_rect)

#       play_button.update(screen, mouse_pos)
#       exit_button.update(screen, mouse_pos)
        title.update(screen)

        shadow.update(screen)



        pygame.display.flip()

def wall1():
    score_text = text.Text(X_MID, 25, WIDTH, 35, 40, WHITE, (0,0,0), "L L A V E S: " + str(score) + " / 3")
    bg_image = pygame.image.load("wall1.jfif")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))




    door1 = pygame.image.load("door1.jpg").convert_alpha()
    door1_rect = door1.get_rect()
    door1_rect.topleft = (200,260)

    while True:

        screen.blit(bg_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if left_button.rect.collidepoint(event.pos):
                        wall4()
                    if right_button.rect.collidepoint(event.pos):
                        wall2()
                    if door1_rect.collidepoint(event.pos) and not (puzzle1_solved):
                        fade(WIDTH, HEIGHT)
                        door1_puzzle()

        left_button.update(screen, mouse_pos)
        right_button.update(screen, mouse_pos)
        screen.blit(door1, door1_rect)

        score_text.update(screen)

        

        pygame.display.flip()

def wall2():
    score_text = text.Text(X_MID, 25, WIDTH, 35, 40, WHITE, (0,0,0), "L L A V E S: " + str(score) + " / 3")

    bg_image = pygame.image.load("wall2.jfif")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))




    door2 = pygame.image.load("door2.jpg").convert_alpha()
    door2_rect = door2.get_rect()
    door2_rect.topleft = (330,260)
    while True:

        screen.blit(bg_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if left_button.rect.collidepoint(event.pos):
                        wall1()
                    if right_button.rect.collidepoint(event.pos):
                        wall3()
                    if door2_rect.collidepoint(event.pos) and not (puzzle2_solved):
                        fade(WIDTH, HEIGHT)
                        door2_puzzle()

        left_button.update(screen, mouse_pos)
        right_button.update(screen, mouse_pos)
        screen.blit(door2, door2_rect)

        score_text.update(screen)
        
        pygame.display.flip()

def wall3():
    score_text = text.Text(X_MID, 25, WIDTH, 35, 40, WHITE, (0,0,0), "L L A V E S: " + str(score) + " / 3")

    bg_image = pygame.image.load("wall3.jfif")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))



    door3 = pygame.image.load("door3.jpg").convert_alpha()
    door3_rect = door3.get_rect()
    door3_rect.topleft = (320,260)
    while True:

        screen.blit(bg_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if left_button.rect.collidepoint(event.pos):
                        wall2()
                    if right_button.rect.collidepoint(event.pos):
                        wall4()
                    if door3_rect.collidepoint(event.pos) and not (puzzle3_solved):
                        fade(WIDTH, HEIGHT)
                        door3_puzzle()

        left_button.update(screen, mouse_pos)
        right_button.update(screen, mouse_pos)
        screen.blit(door3, door3_rect)

        score_text.update(screen)


        pygame.display.flip()


def wall4():
    global score
    
    score_text = text.Text(X_MID, 25, WIDTH, 35, 40, WHITE, (0,0,0), "L L A V E S: " + str(score) + " / 3")
    popup_text = text.Text(X_MID, Y_MID, WIDTH / 3, 50, 40, WHITE, (0,0,0), "Necesitas 3 llaves para salir")


    bg_image = pygame.image.load("wall4.jfif")
    bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))




    door4 = pygame.image.load("door4.jpg").convert_alpha()
    door4_rect = door4.get_rect()
    door4_rect.topleft = (340,230)

    show_popup = False
    
    while True:

        screen.blit(bg_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if left_button.rect.collidepoint(event.pos):
                        wall3()
                    if right_button.rect.collidepoint(event.pos):
                        wall1()

                    if door4_rect.collidepoint(event.pos):
                        if score < 3:
                            show_popup = True
                            
                        else:
                            door4_rect.width = 50
                            door4_rect.height = 100

                            for i in range(1000):
                                door4_rect.width +=  1.5
                                door4_rect.height +=  3
                                door4_rect.center = (X_MID-120, Y_MID)
                                pygame.draw.rect(screen, GREY, door4_rect)
                                pygame.time.delay(1)
                                pygame.display.flip()
                            score = 0
                            main_menu()




        left_button.update(screen, mouse_pos)
        right_button.update(screen, mouse_pos)
        screen.blit(door4, door4_rect)

        score_text.update(screen)

        if show_popup:
            popup_text.update(screen)

        pygame.display.flip()

def door1_puzzle():
    global score
    global puzzle1_solved
    
    set_size = HEIGHT / 2
    
    title = text.Text(X_MID,90,WIDTH, 45, 50, BLACK, WHITE, "PUZZLE 1: CONJUNTOS")
    set1_even = sets.Set(X_MID - set_size/3.5,Y_MID - 20, set_size, SET1, BLACK)
    set2_prime = sets.Set(X_MID + set_size/3.5,Y_MID - 20, set_size, SET2, BLACK)

    set1_text = text.Text(X_MID-100 -set_size/2,Y_MID- 30 - set_size/2, 250, 40, 35, BLACK, WHITE, "NUMEROS PARES")
    set2_text = text.Text(X_MID+100 +set_size/2,Y_MID- 30 - set_size/2, 250, 40, 35, BLACK, WHITE, "NUMEROS PRIMOS")

    win_text = text.Text(X_MID, Y_MID, WIDTH, HEIGHT/2, 40, BLACK, WHITE, "...")


    cards = []
    x = 50
    y = HEIGHT - 120
    cards_nums = [2,3,4,5,7,10]
    num_cards = len(cards_nums)
    solved = False

    distance = WIDTH / (num_cards + 1)

    dragging_index = None
    
    for i in range(1, num_cards + 1):
        card = cards_set.Card(distance * (i),y, cards_nums[i-1])
        
        cards.append(card)
        
    while True:

        screen.fill(PUZZLE1)
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(event.pos):
                        fade(WIDTH, HEIGHT)
                        wall1()

                    for num, card in enumerate(cards):
                        if card.rect.collidepoint(event.pos):
                            dragging_index = num

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging_index = None
        
                

            if event.type == pygame.MOUSEMOTION:
                if dragging_index != None:
                    cards[dragging_index].rect.move_ip(event.rel)
                    
        for card in cards:
            if card.rect.colliderect(set1_even.rect):
                if card.number not in set1_even.nums:
                    set1_even.nums.append(card.number)
            else:
                if card.number in set1_even.nums:
                    set1_even.nums.remove(card.number)

            if card.rect.colliderect(set2_prime.rect):
                if card.number not in set2_prime.nums:
                    set2_prime.nums.append(card.number)
            else:
                if card.number in set2_prime.nums:
                    set2_prime.nums.remove(card.number)

            solved = is_puzzle1_solved(cards_nums, set1_even.nums, set2_prime.nums)



        set1_contents = text.Text(WIDTH/3 -30,HEIGHT - 40, 400, 35, 40, BLACK, WHITE, str(set1_even.nums) )
        set2_contents = text.Text((WIDTH/3 * 2)+30, HEIGHT - 40, 400, 35, 40, BLACK, SET2, str(set2_prime.nums) )
        

        title.update(screen)
        back_button.update(screen, mouse_pos)
        set1_text.update(screen)
        set2_text.update(screen)
            
        set1_even.update(screen)
        set2_prime.update(screen)

        set1_contents.update(screen)
        set2_contents.update(screen)

        for card in cards:
            card.update(screen)

        if solved:
            score += 1
            puzzle1_solved = True
            for i in range(1300):
                win_text.width = i *1.3
                win_text.height = i
                win_text.update(screen)
                pygame.time.delay(1)
                pygame.display.flip()

            solved_screen_puzzle(1)

            

        
        pygame.display.flip()




    
def door2_puzzle():
    global score
    global puzzle2_solved

    
    title = text.Text(X_MID,90,WIDTH, 45, 50, BLACK, WHITE, "PUZZLE 2: RELACIONES")
    ellipse1 = ellipse.Ellipse(WIDTH / 4, Y_MID+85, HEIGHT/2.6, HEIGHT/1.6, WHITE, [1,2,3,4])
    ellipse2 = ellipse.Ellipse((WIDTH / 4) * 3, Y_MID+85, HEIGHT/2.6, HEIGHT/1.6, PUZZLE1, [2,4,6,8])
    win_text = text.Text(X_MID, Y_MID, WIDTH, HEIGHT/2, 40, BLACK, WHITE, "...")

    ellipse1_text = text.Text(WIDTH/6, Y_MID - 180, 50, 50, 40, WHITE, PUZZLE1, "A" )
    ellipse2_text = text.Text(WIDTH/6 * 5, Y_MID - 180, 50, 50, 40, BLACK, WHITE, "B" )

    explanation = """Relaciona el conjunto A con el B si el número de B es divisible entre el número de A. (b%a = 0)"""

    explanation_text = text.Text(X_MID, Y_MID - 270, 1200, 35, 34, BLACK, WHITE, explanation )



    connecting = False
    mouse_pos = pygame.mouse.get_pos()
    item_clicked = None

    line_relations = []
    relations = []
    solved = False

    
    while True:

        screen.fill(PUZZLE2)
        mouse_pos = pygame.mouse.get_pos()



            

        title.update(screen)
        back_button.update(screen, mouse_pos)
        ellipse1.update(screen)
        ellipse2.update(screen)

                #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(event.pos):
                        fade(WIDTH, HEIGHT)
                        wall2()

                    for card in ellipse1.num_cards:
                        if card.rect.collidepoint(event.pos) and connecting == False:
                            connecting = True
                            item_clicked = card
                            item1_pos = (card.rect.x+card.size/2, card.rect.y+card.size/2)
                            break
                        elif card.rect.collidepoint(event.pos) and connecting == True:
                            connecting = False
                            item_clicked = None

                                
                    for card in ellipse2.num_cards:
                        
                        if card.rect.collidepoint(event.pos) and connecting == True:
                            to_item = card
                            relation = [item_clicked.number, to_item.number]

                            if relation not in relations:
                                relations.append(relation)
                                line_relation = [item_clicked.get_pos(), to_item.get_pos()]
                                line_relations.append(line_relation)


                            connecting = False
                            
                if event.button == 3:
                    for card_index in range(len(ellipse2.num_cards)):
                        card = ellipse2.num_cards[card_index]
                        if card.rect.collidepoint(event.pos):
                            for relation_index in range(len(relations)-1, -1, -1):
                                if relations[relation_index][1] == card.number:
                                    relations.pop(relation_index)
                                    line_relations.pop(relation_index)
                                    break
                    connecting = False
                    item_clicked = None   
        
        if connecting:
            pygame.draw.line(screen,BLACK,item1_pos,mouse_pos,5)

        for relation in line_relations:
            start = relation[0]
            end = relation[1]
            pygame.draw.line(screen,BLACK,start,end,5)

        solved = is_puzzle2_solved(ellipse1, ellipse2, relations)

        if solved:
            score += 1
            puzzle2_solved = True
            for i in range(1300):
                win_text.width = i *1.3
                win_text.height = i
                win_text.update(screen)
                pygame.time.delay(1)
                pygame.display.flip()

            solved_screen_puzzle(2)
       

        relations_text = text.Text(X_MID, HEIGHT -40, 900, 40, 35, BLACK, WHITE, str(relations))
        relations_text.update(screen)

        ellipse1_text.update(screen)
        ellipse2_text.update(screen)
        explanation_text.update(screen)
        pygame.display.flip()

def door3_puzzle():
    global score
    global puzzle3_solved
    
    title = text.Text(X_MID,90,WIDTH, 45, 50, WHITE, BLACK, "PUZZLE 3: FUNCIONES")
    win_text = text.Text(X_MID, Y_MID, WIDTH, HEIGHT/2, 40, BLACK, WHITE, "...")

    solved = False


    


    functions_texts = []

    nums = [2, 4, 7]
    nums_answers = [5, 9 , 15]

    num_questions = len(nums)

    inputs_texts = []
    arrows_left = []
    arrows_right = []
    distance = HEIGHT / (num_questions + 4)
    distance_x = WIDTH / (num_questions + 1)

    cards = []

    space_list = []
    bottom = spaces.Space(X_MID, HEIGHT, WIDTH + 20, HEIGHT/3, GREY)

    dragging = False
    card_dragging = None

    answers = []

    for i in range(num_questions):
        answers.append(0)




    for i in range(num_questions):
        function_text = text.Text(WIDTH / 6 *3,(distance * (i+1)) + 110, WIDTH / 5,35, 40, BLACK, (230,230,230), "f(x) = 2x+1" )
        functions_texts.append(function_text)

        input_text = text.Text(WIDTH / 6 * 1,(distance * (i+1)) + 110, WIDTH / 10,35, 35, BLACK, (230,230,230), str(nums[i]) )
        inputs_texts.append(input_text)

        arrow_left = text.Text(WIDTH / 6 * 2,(distance * (i+1)) + 110, WIDTH / 12,30, 35, BLACK, ORANGE, "->")
        arrows_left.append(arrow_left)

        arrow_right = text.Text(WIDTH / 6 * 4,(distance * (i+1)) + 110, WIDTH / 12,30, 35, BLACK, ORANGE, "->")
        arrows_right.append(arrow_right)

        space = spaces.Space(WIDTH / 6 * 5, ((distance) * (i+1)) + 110, WIDTH / 8.5, 55, GREY)
        space_list.append(space)

        card = cards_set.Card2(distance_x * (i+1), HEIGHT / 10 * 9, WIDTH/10, 35, 40,str(nums_answers[i]), BLACK, ORANGE)
        cards.append(card)

    while True:
        for i, scape in enumerate(space_list):
            answers[i] = scape.number

    

        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


                            

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
                    card_dragging = None
        
        

            if event.type == pygame.MOUSEMOTION:
                if card_dragging != None:
                    mouse_pos = pygame.mouse.get_pos()
                    card_dragging.x = mouse_pos[0]
                    card_dragging.y = mouse_pos[1]

                    for space in space_list:
                        if card_dragging.rect.colliderect(space.rect) and space.full == False:
                            card_dragging.locked = True
                            card_dragging.x = space.x
                            card_dragging.y = space.y
                            
                            card_dragging.space_using = space
                            card_dragging.space_using.full = True
                            card_dragging.locked = True
                            
                            card_dragging.space_using.number = card_dragging.number

                            dragging = False
                            card_dragging = None

                            break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(event.pos) :
                        fade(WIDTH, HEIGHT)
                        wall3()

                    for card in cards:
                        if card.rect.collidepoint(event.pos) and  card.locked == False:
                            dragging = True
                            card_dragging = card
                            break
 
                if event.button == 3:
                    for card in cards:
                        if card.rect.collidepoint(event.pos) and card.locked == True:
                            card.x = card.initial_x
                            card.y = card.initial_y
                            card.locked = False
                            card.space_using.full = False
                            card.space_using.number = 0
                            card.space = None
                            
                            break



        title.update(screen)
        back_button.update(screen, mouse_pos)

        for function_text in functions_texts:
            function_text.update(screen)

        for input_text in inputs_texts:
            input_text.update(screen)

        for arrow_left in arrows_left:
            arrow_left.update(screen)

        for arrow_right in arrows_right:
            arrow_right.update(screen)

        for space in space_list:
            space.update(screen)

        bottom.update(screen)

        for card in cards:
            card.update(screen)

        solved = is_puzzle3_solved(nums, answers)

        if solved:
            score += 1
            puzzle3_solved = True
            for i in range(1300):
                win_text.width = i *1.3
                win_text.height = i
                win_text.update(screen)
                pygame.time.delay(1)
                pygame.display.flip()
            solved_screen_puzzle(3)


        pygame.display.flip()

def door4_puzzle():
    title = text.Text(X_MID,90,WIDTH, 45, 50, BLACK, WHITE, "PUZZLE 4:")
    while True:

        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(event.pos):
                        fade(WIDTH, HEIGHT)
                        wall4()

        title.update(screen)
        back_button.update(screen, mouse_pos)
        
        

        pygame.display.flip()
    

def solved_screen_puzzle(room):
    title = text.Text(X_MID,Y_MID,WIDTH, HEIGHT, 100, BLACK, WHITE, "LLAVES: " + str(score) + " / 3")
    while True:

        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        #LOOK FOR EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if back_button.rect.collidepoint(event.pos):
                        fade(WIDTH, HEIGHT)
                        if room == 1:
                            wall1()
                        elif room == 2:
                            wall2()
                        elif room == 3:
                            wall3()
                        elif room == 4:
                            wall4()

        title.update(screen)
        back_button.update(screen, mouse_pos)
        

        pygame.display.flip()
    

main_menu()
pygame.quit()


    
    
