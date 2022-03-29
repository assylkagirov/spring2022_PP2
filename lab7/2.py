import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Music Player")
playing = True
songs = ["1.mp3", "2.mp3", "3.mp3"]
queue = 0
tick = 0
prevqueue = 2130
once = True
prevstate = ""
needUpdate = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            if event.key == pygame.K_LEFT:
                if queue == 0:
                    queue = 2
                else:
                    queue -= 1 
            if event.key == pygame.K_RIGHT:
                if queue == 2:
                    queue = 0
                else:
                    queue += 1
    screen.fill((0, 0, 0))
    pygame.display.flip()
    state = playing and "Pause" or "Unpause"
    if needUpdate or state != prevstate:
        caption = "Current track: " + str(queue + 1) + ".mp3. State: " + state + " | Space = Pause/Unpause | Right Arrow = Next | Left Arrow = Previous"
        prevstate = state
        pygame.display.set_caption(caption)
        needUpdate = False
    if prevqueue != queue:
        pygame.mixer.music.load(songs[queue])
        if playing:
            pygame.mixer.music.play()
        prevqueue = queue
        needUpdate = True
