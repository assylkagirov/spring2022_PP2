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
SCREEN_WIDTH, SCREEN_HEIGHT, SPEED, SCORE, COINSCORE, LEVEL = 400, 600, 5, 0, 0, 10
 
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
    cointype = 's'
    randomint = 0
    def __init__(self):
        super().__init__()
        self.randomint = random.randint(0, 10) #generate random coin weight
        if self.randomint == (0 or 1 or 2 or 3 or 4):
            self.image = pygame.image.load("SmallCoin.png")
            self.cointype = 's'
        elif self.randomint == (5 or 6 or 7):
            self.image = pygame.image.load("MediumCoin.png")
            self.cointype = 'm'
        elif self.randomint == (8 or 9):
            self.image = pygame.image.load("BigCoin.png")
            self.cointype = 'b'
        self.image = pygame.image.load("SmallCoin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), SCREEN_HEIGHT - 80)  

    def disappear(self):
        global COINSCORE
        # check different weight
        if self.cointype == 's':
            COINSCORE += 1
        elif self.cointype == 'm':
            COINSCORE += 3
        elif self.cointype == 'b':
            COINSCORE += 5
        self.randomint = random.randint(0, 10) ##recreating new coin type
        if self.randomint == (0 or 1 or 2 or 3 or 4):
            self.image = pygame.image.load("SmallCoin.png")
            self.cointype = 's'
        elif self.randomint == (5 or 6 or 7):
            self.image = pygame.image.load("MediumCoin.png")
            self.cointype = 'm'
        elif self.randomint == (8 or 9):
            self.image = pygame.image.load("BigCoin.png")
            self.cointype = 'b'
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

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  
            #print('%s' % (str(SPEED)))
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
        if COINSCORE >= LEVEL:
            SPEED += 0.5 #enemy speed increase every 10 coins
            LEVEL += 10 #increase level to not get in infinity
            #print('%s' % (str(SPEED)))
    pygame.display.update()
    FramePerSec.tick(FPS)