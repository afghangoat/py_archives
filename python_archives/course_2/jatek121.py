import pygame
import random
pygame.init()

timer=pygame.time.Clock()
font = pygame.font.SysFont('Arial',50)
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,0)
dis_width = 800
dis_height =600
snake_block = 10
snake_speed = 20
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.update()
pygame.display.set_caption('Snake')
gameover=False
x1= dis_width/2
y1= dis_height/2
x1_change = 0
y1_change = 0
foodx=round(random.randrange(0,dis_width-snake_block)/10)*10
foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
def message(msg,color):
    text=font.render(msg,True,color)
    dis.blit(text,[dis_width/2,dis_height/2])
    pygame.display.update()
def our_snake(snake_block,slist):
    for x in slist:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])
slist=[]
los=1
while not gameover:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            if event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = snake_block
            if event.key ==pygame.K_UP:
                x1_change=0
                y1_change=-snake_block

    if x1>=dis_width or y1 <0 or x1 <0 or y1>dis_height:
         gameover=True
         message("Game Over",red)
         timer.sleep(2)
    x1+=x1_change
    y1+=y1_change
    dis.fill(white)
    if x1 == foodx and y1==foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10) * 10
        foody = round(random.randrange(0, dis_height - snake_block) / 10) * 10
        los +=1
    pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
    pygame.draw.rect(dis,black,[x1,y1,snake_block,snake_block])
    snake_head=[x1,y1]
    slist.append(snake_head)
    if len(slist) > los:
        del slist[0]
    our_snake(snake_block,slist)
    pygame.display.update()
    timer.tick(snake_speed)
pygame.quit()
quit()