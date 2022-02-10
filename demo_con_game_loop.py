import pygame
import random
pygame.init()

COLOR = (0, 200, 100)
radio=100

SIZE = (640,420)
screen = pygame.display.set_mode(SIZE)

sonido = pygame.mixer.Sound("whiff.wav")
sonido.play()

clock = pygame.time.Clock()

continuar=True
x=100
y=100
while continuar:

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            continuar=False
  
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        sonido.play()    
    if keystate[pygame.K_LEFT]:
        x-=1
    if keystate[pygame.K_RIGHT]:
        x+=1
    if keystate[pygame.K_UP]:
        y-=1
    if keystate[pygame.K_DOWN]:
        y+=1
    screen.fill((0,0,0))    
    pygame.draw.circle(screen, COLOR,(x,y),radio)   
    pygame.draw.rect(screen, COLOR,(10,10,50,50),2)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()

exit();
