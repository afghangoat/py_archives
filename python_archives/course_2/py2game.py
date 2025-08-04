import pygame
import os
import math
import random
WIDTH = 900
METEOR_WIDTH = 50
METEOR_HEIGHT= 50
HEIGHT = 500
WINDOW=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Space Fight')
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
pygame.font.init()
pygame.mixer.init()
HEALTH_FONT=pygame.font.SysFont("Comic Sans MS", 40)
WINNER_FONT=pygame.font.SysFont("Comic Sans MS", 100)
BORDER=pygame.Rect(WIDTH//2,0,10,HEIGHT)
METEOR_IMAGE = pygame.image.load('Assets/meteor.png')
meteor1=pygame.transform.rotate(pygame.transform.scale(METEOR_IMAGE,(METEOR_WIDTH,METEOR_HEIGHT)),90)
FPS=60
METEOR_DIR=random.randint(0,359)
METEOR_Y_VEL=math.cos(METEOR_DIR)*2
METEOR_X_VEL=math.sin(METEOR_DIR)*2
VEL=5
MAX_BULLETS=3
BULLET_VEL=7
SPACESHIP_WIDTH=80
SPACESHIP_HEGIHT=60


YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2

SPACE_BACKGROUND=pygame.image.load('Assets/space.png')
sound1=pygame.mixer.Sound('Assets/explosion.wav')
YELLOW_SPACESHIP_IMAGE=pygame.image.load('Assets/spaceship_yellow.png')
RED_SPACESHIP_IMAGE=pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP=pygame.transform.rotate(
pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEGIHT)), 270)
YELLOW_SPACESHIP=pygame.transform.rotate(
pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEGIHT)), 90)
def yellow_control(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x-VEL > -15:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL+yellow.width-35 < BORDER.x:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y-VEL > -10:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y+VEL+yellow.height < HEIGHT:
        yellow.y += VEL
def red_control(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x-VEL > BORDER.x:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x+VEL < WIDTH-50:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y-VEL > -10:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y+VEL+red.height < HEIGHT:
        red.y += VEL
def drawWindow(red,yellow,red_bullets,yellow_bullets,yellow_health,red_health):
    #WINDOW.fill(WHITE)
    red_health_text=HEALTH_FONT.render(f"Életerő: {red_health}",True, WHITE)
    yellow_health_text = HEALTH_FONT.render(f"Életerő: {yellow_health}", True, WHITE)
    WINDOW.blit(red_health_text,(WIDTH - red_health_text.get_width() -10,10))
    WINDOW.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))
    pygame.draw.rect(WINDOW,BLACK,BORDER)
    WINDOW.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))
    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WINDOW,RED,bullet)
    pygame.display.update()
def handle_bullets(rb,yb,yellow,red):
    for bullet in yb:
        bullet.x -= BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yb.remove(bullet)
        elif bullet.x > WIDTH:
            yb.remove(bullet)
    for bullet in rb:
        bullet.x+=BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            rb.remove(bullet)
        elif bullet.x < -15:
            rb.remove(bullet)
def drawWinner(text):
    textbox=WINNER_FONT.render(text,True,WHITE)
    WINDOW.blit(textbox,(WIDTH/2 - textbox.get_width() / 2, HEIGHT/2 - textbox.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)
def main():

    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_WIDTH)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_WIDTH)

    yellow_bullets=[]
    red_bullets=[]

    clock = pygame.time.Clock()
    run=True
    red_health=10
    yellow_health=10
    while(run):
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.height, yellow.y + yellow.width // 2, 10, 5)
                    yellow_bullets.append(bullet)
                    sound1.play()
                if event.key == pygame.K_RCTRL and len(red_bullets)<MAX_BULLETS:
                    bullet=pygame.Rect(red.x+yellow.height,red.y+red.width//2,10,5)
                    red_bullets.append(bullet)
                    sound1.play()
            if event.type == pygame.YELLOW_HIT:
                yellow_health -= 1
                sound1.play()
            if event.type==pygame.RED_HIT:
                yellow_health-=1
                sound1.play()
        winner_text=""
        if yellow_health <= 0:
            winner_text = "Red Won!"
        if red_health <= 0:
            winner_text = "Yellow Won!"
        if winner_text != "":
            drawWinner(winner_text)
            run=False
        #yellow.x+=1
        keys_pressed=pygame.key.get_pressed()
        red_control(keys_pressed,red)
        yellow_control(keys_pressed, yellow)
        handle_bullets(yellow_bullets,red_bullets,yellow,red)
        drawWindow(red,yellow,red_bullets,yellow_bullets,yellow_health,red_health)
    pygame.quit()

if __name__=="__main__":
    main()

