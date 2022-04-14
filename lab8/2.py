import pygame, random

pygame.init()

blue, red, black, yellow, green = (0, 0, 255), (255, 0, 0), (0, 0, 0), (255,255,102), (0,255,0)

dis_width, dis_height = 800, 600

dis = pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption("Snake")

snake_block, snake_speed, level = 10, 20, 1 #game vars

clock = pygame.time.Clock()

font_style, score_font = pygame.font.SysFont("papyrusttc", 50), pygame.font.SysFont("papyrusttc", 25)

def display_score(score, level):
    value = score_font.render("Level: " + str(level) + " Your score: " + str(score), True, yellow) #level and score counter
    dis.blit(value, [0,0])

def draw_snake(snake_block, snake_list):
    for item in snake_list:
        pygame.draw.rect(dis, black, [item[0], item[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2
    
    x1_change = 0
    y1_change = 0
    snake_block, snake_speed, level = 10, 20, 1
    snake_list = []
    snake_length = 1
    #making food x and y first time
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 
    #print("foodx: %d foody: %d" % (foodx, foody)) debug food pos
    while not game_close:

        while game_over == True:
            dis.fill(blue)
            message("game over!", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = False
                        game_close = True
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        #if statements for checking if snake passes to other side
        if x1 >= dis_width:
            x1 = 0 
        if x1 < 0:
            x1 = dis_width 
        if y1 >= dis_height:
            y1 = 0
        if y1 < 0:
            y1 = dis_height
        #level up statement
        if snake_length > (level * 4):
            level += 1
            snake_speed += 5
        x1 += x1_change
        y1 += y1_change


        dis.fill(blue)
  
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) 

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)

        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        iterations = 0
        for snakepos in snake_list: #check if you collide with yourself to finish the game
            if iterations != 0:
                #print("Anypos: ", snakepos) debug
                #print("Current: ", snake_list[0]) debug
                if snakepos == snake_list[0]:
                    game_over = True
            iterations += 1
        draw_snake(snake_block, snake_list)

        display_score(snake_length - 1, level)
   

        pygame.display.update()
        
        if x1 == foodx and y1 == foody:
            #making food x and y after you ate one
            foodx = round(random.randrange(0, dis_width) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height) / 10.0) * 10.0     
            snake_length += 1

        clock.tick(snake_speed)
            
    pygame.quit()
    quit()

gameLoop()