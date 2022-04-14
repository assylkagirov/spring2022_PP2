#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS, FramePerSec = 60, pygame.time.Clock()
 
#Creating colors
BLUE, RED, GREEN, BLACK, WHITE = (0, 0, 255), (255, 0, 0), (0, 255, 0), (0, 0, 0), (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH, SCREEN_HEIGHT, SPEED, SCORE, COINSCORE = 400, 600, 5, 0, 0
 
#Setting up Fonts
font, font_small = pygame.font.SysFont("Verdana", 60), pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#creating coin class (somewhat similar to enemy)                    
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), SCREEN_HEIGHT - 80)  

    def disappear(self):
        global COINSCORE
        COINSCORE += 1 #increment coin score
        self.rect.move_ip(SCREEN_HEIGHT - 80,200) 
        self.rect.top = SCREEN_HEIGHT - 80
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), SCREEN_HEIGHT - 80)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
 
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    coinscores = font_small.render(str(COINSCORE), True, BLACK) # show collected coins
    DISPLAYSURF.blit(coinscores, (SCREEN_WIDTH - 30,10))
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    for coin in coins:
        DISPLAYSURF.blit(coin.image, coin.rect) #re-drawing coins
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    if pygame.sprite.spritecollideany(P1, coins): #collide with coins
        pygame.mixer.Sound('bell.wav').play() #song when coin picked up
        pygame.display.update()
        C1.disappear() #trigger coin reappear

    pygame.display.update()
    FramePerSec.tick(FPS)