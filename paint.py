import pygame

########################################
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BGCOLOR = (255,255,255)
BRUSHCOLOR = (0,0,0)
BRUSHSIZE = 4
#######################################

pygame.init()
win = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption("Paint")
win.fill(BGCOLOR)
pygame.display.flip()

def paint(win,mousex,mousey):
    pygame.draw.circle(win, BRUSHCOLOR, (mousex,mousey), BRUSHSIZE)


isPressed = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            isPressed = False
        if event.type == pygame.MOUSEMOTION and isPressed == True:
            (mousex,mousey) = pygame.mouse.get_pos()
            paint(win,mousex,mousey)
    pygame.display.flip()
