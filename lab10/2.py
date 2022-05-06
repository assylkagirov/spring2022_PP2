import pygame, random, time
import psycopg2
from psycopg2 import Error


pygame.init()

blue, red, black, yellow, green, grellow = (0, 0, 255), (255, 0, 0), (0, 0, 0), (255,255,102), (0,255,0), (160,255,88)

dis_width, dis_height = 800, 600

dis = pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption("Snake")

snake_block, snake_speed, level = 10, 20, 1 #game vars

try:
    connection = psycopg2.connect(user="postgres",
                                  password="joker123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    
    print("Enter username: ")
    username = str(input())
    cursor.execute(f'''INSERT INTO game (user, user_level) VALUES('{username}', 0)''')
    connection.commit()
        
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

clock = pygame.time.Clock()
timeredfood = False
timint = 0
timer = 0
font_style, score_font = pygame.font.SysFont("papyrusttc", 50), pygame.font.SysFont("papyrusttc", 25)

def display_score(score, level):
    if timeredfood:
        value = score_font.render("Level: " + str(level) + " Your score: " + str(score) + " Food Disappear: " + str(timint + timer - int(time.time())), True, yellow) #level and score and timer counter
    else:
        value = score_font.render("Level: " + str(level) + " Your score: " + str(score), True, yellow) #level and score counter
    dis.blit(value, [0,0])


def draw_snake(snake_block, snake_list):
    for item in snake_list:
        pygame.draw.rect(dis, black, [item[0], item[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

foodtype = 0
randomint = 0
def gameLoop():
    game_over = False
    game_close = False
    
    x1 = dis_width / 2
    y1 = dis_height / 2
    
    x1_change = 0
    y1_change = 0
    global snake_block, snake_speed, level, randomint, timeredfood, timer, timint
    
    snake_list = []
    snake_length = 1
    #making food x and y first time
    foodx = round(random.randrange(10, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(10, dis_height - snake_block) / 10.0) * 10.0 
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

        global foodtype
        dis.fill(blue)
        # randomization of rarity of food
        if randomint == 0 or randomint == 1 or randomint == 2 or randomint == 3 or randomint == 4:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            foodtype = 0
        elif randomint == 5 or randomint == 6 or randomint == 7:
            pygame.draw.rect(dis, grellow, [foodx, foody, snake_block, snake_block]) 
            foodtype = 1
        elif randomint == 8 or randomint == 9:
            pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block]) 
            foodtype = 2
        elif randomint == 10:
            pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])   
            foodtype = 3  
        print('%d %d' % (foodx, foody))
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
            foodx = round(random.randrange(10, dis_width) / 10.0) * 10.0
            foody = round(random.randrange(10, dis_height) / 10.0) * 10.0
            if foodtype == 0: # check food weight
                snake_length += 1
            elif foodtype == 1:
                snake_length += 3
            elif foodtype == 2:
                snake_length += 5
            elif foodtype == 3:
                snake_length += 10
            randomint = random.randint(0, 10) #random next food
            if timeredfood == True:
                timeredfood = False
            if randomint != 0 and randomint % 2 == 0 and timeredfood == False:
                timeredfood = True
                timint = int(time.time())
        #timer food
        if timeredfood:
            if foodtype == 0:
                timer = 15
            elif foodtype == 1:
                timer = 10
            elif foodtype == 2:
                timer = 7
            elif foodtype == 3:
                timer = 4
            if int(time.time()) == timint + timer: # check timer
                timeredfood = False
                #if didnt ate in time generate new
                foodx = round(random.randrange(0, dis_width) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height) / 10.0) * 10.0
                randomint = random.randint(0, 10) #random next food
        clock.tick(snake_speed)
    cursor.execute(f'''INSERT INTO game (user,user_level) VALUES('{username}', '{level}')''')
    connection.commit()
    pygame.quit()
    quit()

gameLoop()
