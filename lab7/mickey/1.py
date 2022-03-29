import datetime, pygame

def blitRot(s, i, t, a):
    r = pygame.transform.rotate(i, a)
    n = r.get_rect(center = i.get_rect(topleft = t).center)
    s.blit(r, n)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")
pygame.display.set_icon(pygame.image.load('1.png'))
mickey_clock, minute_arm, second_arm = pygame.image.load('mickey.png'), pygame.image.load('minutes.png'), pygame.image.load('seconds.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pos = (-100, -100)
    screen.blit(mickey_clock, pos)
    sys_time = datetime.datetime.now()
    blitRot(screen, minute_arm, pos, -(sys_time.minute) * 6)
    blitRot(screen, second_arm, pos, -(sys_time.second) * 6)
    pygame.display.flip()