import pygame,sys,math
pygame.init()
screen = pygame.display.set_mode([1000,1000])
img = pygame.image.load('ball.png')
img1=pygame.transform.scale(img,(75,75))
rect=screen.get_rect()
clock = pygame.time.Clock()
X,Y=102,681
dx,dy=2,0
plotPoints = [(102,681)]
i=-1
angle=0
while True:
    i=i+1
    angle=angle-5
    screen.fill('gold')
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    X=X+dx
    Y=int(math.sin(X/640.0 * 4 * math.pi) * 200 )+500
    img2=pygame.transform.rotate(img1,angle)
    rect=img2.get_rect(center=(X,Y))
    plotPoints.append([X,Y])
    
    pygame.draw.lines(screen,(255,0,0),False, plotPoints, 3)
    
    if X>1000:
        plotPoints.clear()
        plotPoints = [(102,681)]
        X,Y=102,681
    
    
    screen.blit(img2,rect)
    #pygame.draw.rect(screen,'gold',rect,4)
    pygame.display.update()
    clock.tick(60)
    



    
    


 
 
