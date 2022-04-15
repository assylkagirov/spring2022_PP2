import pygame
pygame.display.set_caption("Current mode: Brush. Current color: Blue." + "; c=circle; p=rectangle; l=brush; r=red; g=green; b=blue")
data = []
elements = 0
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'Blue'
    drawmode = 'Brush'
    oldmode = 'Brush'
    oldcmode = 'Blue'
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'Red'
                elif event.key == pygame.K_g:
                    mode = 'Green'
                elif event.key == pygame.K_b:
                    mode = 'Blue'
                #checking shapes
                if event.key == pygame.K_l:
                    drawmode = 'Brush'
                elif event.key == pygame.K_c:
                    drawmode = 'Circle'
                elif event.key == pygame.K_p:
                    drawmode = 'Rectangle'
                if oldmode != drawmode:
                    oldmode = drawmode
                    pygame.display.set_caption("Current mode: "+drawmode+" Current color: "+mode+ "; c=circle; p=rectangle; l=brush; r=red; g=green; b=blue") #update paint status
                if oldcmode != mode:
                    oldcmode = mode
                    pygame.display.set_caption("Current mode: "+drawmode+" Current color: "+mode+ "; c=circle; p=rectangle; l=brush; r=red; g=green; b=blue") #update paint status
            screen.fill((0, 0, 0))    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #check if clicked then add to draw
                    drawadd(event.pos, radius, mode, drawmode)
                if event.button == 4: #check mousewhell to incr/decr the radius
                    radius = min(200, radius + 1)
                elif event.button == 5:
                    radius = max(1, radius - 1)
                
        draw(screen)
        pygame.display.flip()
        
        clock.tick(60)

def drawadd(start, width, color_mode, draw_mode): #add to draw function
    global data, elements
    if color_mode == 'Blue': #color kmode
        color = (0, 0, 255)
    elif color_mode == 'Red':
        color = (255, 0, 0)
    elif color_mode == 'Green':
        color = (0, 255, 0)
    clist = [] #creating data list for our drawing
    clist.append(start[0])
    clist.append(start[1])
    clist.append(width)
    clist.append(color)
    clist.append(draw_mode)
    data.append(clist) #appending this list to gen data
    elements += 1

def draw(screen):
    global data, elements #getting global vars
    if elements != 0: #checking if elements exist
        for element in data:
            if element[4] == 'Brush': #checking every possible shape
                pygame.draw.circle(screen, element[3], (element[0], element[1]), element[2])
            elif element[4] == 'Circle':
                pygame.draw.circle(screen, element[3], (element[0], element[1]), element[2], 1)
            elif element[4] == 'Rectangle':
                pygame.draw.rect(screen, element[3], pygame.Rect(element[0], element[1], element[2], element[2] / 2), 1)
            elif element[4] == 'Eraser':
                pygame.draw.circle(screen, (0,0,0), (element[0], element[1]), element[2])
main()
