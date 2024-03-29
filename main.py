from random import *
from pygame import *
from time import time as timer
window = display.set_mode((700,500))

win_witdh = 700
win_height = 500

finish = False

speed_x = 3
speed_y = 3

font.init()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 75)


lose2 = font1.render('PLAYER 2 LOSE', True, (180, 0, 0))
lose1 = font1.render('PLAYER 1 LOSE', True, (180, 0, 0))

background = image.load('background_ping-pong.jpg')
background = transform.scale(background, (700,500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed
ball = GameSprite('tenis_ball.png', 350, 250, 50, 50, randint(1,7))

racket1 = Player('racket.png', 30, 200, 50, 150,4)
racket2 = Player('racket.png', 620, 200, 50, 150,4)

clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background, (0, 0))

        
        racket1.update1()
        racket1.reset()
        racket2.update2()
        racket2.reset()
        ball.reset()
        if ball.rect.x < 60:
            finish = True
            window.blit(lose1, (200, 200))
        if ball.rect.x > 620:
            finish = True
            window.blit(lose2, (200, 200))
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
        speed_x  *= -1
    display.update()
    clock.tick(40)
