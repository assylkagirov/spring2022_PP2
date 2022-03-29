import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
x = 30
y = 30

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
                        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y>30: y-=20
    if pressed[pygame.K_DOWN]: 
        if y<(screen.get_height() - 30): y += 20
    if pressed[pygame.K_LEFT]:
        if x>30: x-=20
    if pressed[pygame.K_RIGHT]: 
        if x<(screen.get_width() - 30): x += 20
        
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    pygame.display.flip()
    clock.tick(60)