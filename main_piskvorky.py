import pygame
import math
from helper import player1, player2

pygame.init()

clock = pygame.time.Clock()

width = (750)
height = (850)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Piškworky")
swamp_screen = pygame.display.set_mode((width, height))

#velikost informacniho pole
inf_field_size = (height - width)
#velikosti oddělující čáry
width_separatting_line = 5

#velikosti kostiček
square_size = (width//15)
square_width = 3
squ_ro_wi = math.sqrt((square_size**2)+(square_size**2))

#color
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128,128,128)
blue =(0, 95, 255)
red =(255, 0, 0)

#font
font = pygame.font.SysFont("Arial", 70)
font2 = pygame.font.SysFont("Arial", 50)

#otazka na swap
levy_obdelnik = (0, 0, width//2, inf_field_size)
pravy_obdelnik = (width//2, 0, width//2, inf_field_size)
#jmena hráčů

player1_name = player1
player2_name = player2
if player1_name == "":
     player1_name = "Player1"
if player2_name == "":
     player2_name = "Player2"
     
p_turn = ""

player1_name_text = font.render(player1_name, True, black, None)
player1_name_rect = player1_name_text.get_rect()
player1_name_rect.topleft = (0, 0)
player2_name_text = font.render(player2_name, True, black, None)
player2_name_rect = player2_name_text.get_rect()
player2_name_rect.topright = (width, 0)


pl_win_text = font.render(f"Hráč {p_turn} vyhrál", True, red, blue)
pl_win_rect = pl_win_text.get_rect()
pl_win_rect.center = (width//2 , height//2 - 100)
question_pl_a_text = font.render("Hrát znovu", True, black, white)
question_pl_a_rect = question_pl_a_text.get_rect()
question_pl_a_rect.midtop = (width//2,height//2)

start_score = 0
score_x = start_score
score_o = start_score
score_shift = 25

#vykreslení score
score_pl1_text = font.render(f"{score_x}", True, black,None)
score_pl1_rect = score_pl1_text.get_rect()
score_pl1_rect.topright =(((width//2)-score_shift), 0)

score_pl2_text = font.render(f"{score_o}", True, black, None)
score_pl2_rect = score_pl2_text.get_rect()
score_pl2_rect.topleft=(((width//2)+score_shift), 0)

halfing_score_text = font.render(":", True, black, None)
halfing_score_rect = halfing_score_text.get_rect()
halfing_score_rect.midtop = ((width//2),0)

who_start_quest_text = font2.render("Kdo začne?", True, black,None)
who_start_quest_rect = who_start_quest_text.get_rect()
who_start_quest_rect.center = (width//2, 200)
start_name1_text = font2.render(player1_name, True, black,None)
start_name1_rect = start_name1_text.get_rect()
start_name1_rect.center = ((width//2 - 100),500)
start_name2_text = font2.render(player2_name, True, black, None)
start_name2_rect = start_name2_text.get_rect()
start_name2_rect.center = ((width//2 + 100),500)


board = [[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None],
         [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None]]

def draw_board():
    for ver in range(15):
        for hor in range(15):
            pygame.draw.rect(screen, grey, (hor * square_size,(ver*square_size) + inf_field_size, square_size, square_size), 2)
            symbol = board[ver][hor]
            if symbol == 'X':
                pygame.draw.line(screen, blue, 
                                 (hor * square_size, ver*square_size + inf_field_size ),
                                  (hor * square_size+square_size, ver*square_size + inf_field_size+square_size), 5)
                
                pygame.draw.line(screen, blue, 
                                 (hor * square_size+square_size ,ver*square_size + inf_field_size ),
                                  (hor * square_size, ver*square_size + square_size + inf_field_size ), 5)
            elif symbol == 'O':
                pygame.draw.circle(screen, red, (hor * square_size + (square_size//2),ver*square_size + inf_field_size+(square_size//2)), (square_size//2-2),4)

def win_line(sx, sy, ex, ey):
    pygame.draw.line(screen, p_turn_colour,(ex, ey),(sx, sy),10)
    pygame.display.update()
    pygame.time.delay(2000)

def win(turn):
    #(w)ho = x
    #(w)ve = y
    for ve in range(15):
        for ho in range(15):
            symbol_w = board[ve][ho]
            if symbol_w == turn:
                win_c = 1
                who = ho
                who += 1
                while board[ve][who] == turn:
                    win_c += 1
                    who += 1
                    if win_c == 5:
                        sx_coor = (who - 5) * square_size 
                        sy_coor = ve * square_size + inf_field_size + square_size //2
                        ex_coor = (who) * square_size 
                        ey_coor = ve * square_size + inf_field_size + square_size //2
                        win_line(sx_coor, sy_coor,ex_coor,ey_coor)
                        return win_c
            if symbol_w == turn:
                win_c = 1
                wve = ve
                wve += 1
                while board[wve][ho] == turn:
                    win_c += 1
                    wve += 1
                    if win_c == 5:
                        sx_coor = (ho * square_size + square_size //2)
                        sy_coor = (wve-5) * square_size + inf_field_size 
                        ex_coor = ho * square_size + square_size //2
                        ey_coor = wve * square_size + inf_field_size 
                        win_line(sx_coor, sy_coor,ex_coor,ey_coor)                       
                        return win_c
            if symbol_w == turn:
                win_c = 1
                who = ho
                wve = ve
                who += 1
                wve += 1
                while board[wve][who] == turn:
                    win_c += 1
                    who += 1
                    wve += 1
                    if win_c == 5:
                        print(wve)
                        print(who)
                        sx_coor = ((who-5) * square_size)
                        sy_coor = (wve-5) * square_size + inf_field_size 
                        ex_coor = who * square_size
                        ey_coor = wve* square_size + inf_field_size 
                        win_line(sx_coor, sy_coor,ex_coor,ey_coor) 
                        return win_c

            if symbol_w == turn:
                win_c = 1
                who = ho
                wve = ve
                who += 1
                wve -= 1
                while board[wve][who] == turn:
                    win_c += 1
                    who += 1
                    wve -= 1
                    if win_c == 5:
                        print(wve)
                        print(who)
                        sx_coor = ((who-5) * square_size)
                        sy_coor = (wve+6) * square_size + inf_field_size
                        ex_coor = (who ) * square_size
                        ey_coor = (wve + 1) * square_size + inf_field_size 
                        win_line(sx_coor, sy_coor,ex_coor,ey_coor) 
                        return win_c
                    
#otazka kdo začne
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(white)
    screen.blit(who_start_quest_text, who_start_quest_rect)
    screen.blit(start_name1_text, start_name1_rect)
    screen.blit(start_name2_text,start_name2_rect)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if start_name1_rect.collidepoint(event.pos):
             p_turn = "X"
             lets_continue = False
        elif start_name2_rect.collidepoint(event.pos):
            p_turn = "O"
            lets_continue = False
    clock.tick(60)
            
    aa,bb = pygame.mouse.get_pos()
    if (start_name1_rect.x <= aa <= (start_name1_rect.x + start_name1_rect[2]) ) and (start_name1_rect.y<= bb <= (start_name1_rect.y + start_name1_rect[3])):
                    start_name1_text = font2.render(player1_name, True, black, grey)
                    screen.blit(start_name1_text,start_name1_rect)  
                    pygame.display.update()
    else:
                    start_name1_text = font2.render(player1_name, True, black, white)
                    screen.blit(start_name1_text, start_name1_rect) 
                    pygame.display.update()
    if (start_name2_rect.x <= aa <= (start_name2_rect.x + start_name2_rect[2]) ) and (start_name2_rect.y<= bb <= (start_name2_rect.y + start_name2_rect[3])):
                    start_name2_text = font2.render(player2_name, True, black, grey)
                    screen.blit(start_name2_text, start_name2_rect)  
                    pygame.display.update()
    else:
                    start_name2_text = font2.render(player2_name, True, black, white)
                    screen.blit(start_name2_text, start_name2_rect)
                    pygame.display.update()

    clock.tick(60)
pygame.time.delay(1000)

#HRA

lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
    
    #barva pozadí
    screen.fill(white)
    score_pl1_text = font.render(f"{score_x}", True, black,None)
    score_pl2_text = font.render(f"{score_o}", True, black,None)
    
    #vykreslení obdelníku hráče co je na řadě
    if p_turn == "X":
        pygame.draw.rect(screen, blue,levy_obdelnik)
        p_turn_colour = blue
    if p_turn == "O":
        pygame.draw.rect(screen,red,pravy_obdelnik)
        p_turn_colour = red
    #halvní obdelník
    pygame.draw.rect(screen, grey,(0, inf_field_size, width, width),5)


    #vykreslení jmen, púlící čáry a score
    screen.blit(player1_name_text, player1_name_rect)
    screen.blit(player2_name_text, player2_name_rect)
    screen.blit(halfing_score_text, halfing_score_rect)
    screen.blit(score_pl1_text, score_pl1_rect)
    screen.blit(score_pl2_text, score_pl2_rect)
    draw_board()
    pygame.display.update()
    clock.tick(60)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lets_continue = False
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (mouse_y > inf_field_size) and ((board[(mouse_y - inf_field_size)// square_size][mouse_x // square_size]) == None):
                    x = mouse_x // square_size
                    y = (mouse_y - inf_field_size)// square_size
                    running = False
        clock.tick(60)
    board[y][x] = p_turn
    draw_board()
    pygame.display.update()
    # výhra
    result = win(p_turn)
    if result == 5:
        if p_turn == "X":
            score_x += 1
            w_line_colour = blue
            p_win = player1_name
        if p_turn == "O":
            score_o +=1
            w_line_colour = red
            p_win = player2_name

        pl_win_text = font.render(f"Hráč {p_win} vyhrál", True, red, blue)
        pl_win_rect = pl_win_text.get_rect()
        pl_win_rect.center = (width//2 , height//2 - 100)
        screen.blit(pl_win_text, pl_win_rect)
        screen.blit(question_pl_a_text, question_pl_a_rect)
        pygame.display.update()

        running = True
        while running:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if question_pl_a_rect.collidepoint(event.pos):
                            for ver in range(15):
                                for hor in range(15):
                                    board[ver][hor] = None
                                    running = False
            a,b = pygame.mouse.get_pos()
            if (question_pl_a_rect.x <= a <= (question_pl_a_rect.x + 338) ) and (question_pl_a_rect.y <= b <= (question_pl_a_rect.y + 80)):
                question_pl_a_text = font.render("Hrát znovu", True, black, grey)
                screen.blit(question_pl_a_text, question_pl_a_rect)  
                pygame.display.update()
            else:
                question_pl_a_text = font.render("Hrát znovu", True, black, white)
                screen.blit(question_pl_a_text, question_pl_a_rect) 
                pygame.display.update()
            clock.tick(60)


                

    if p_turn == "X":
        p_turn = "O"
    elif p_turn == "O":
        p_turn = "X"

    clock.tick(60)
    pygame.display.update()
   
pygame.quit()
