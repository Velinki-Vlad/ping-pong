from random import *
from pygame import *
from time import time as timer
window = display.set_mode((700,500))

win_witdh = 700
win_height = 500

finish = False

font.init()
font1 = font.SysFont(None, 36)
font2 = font.SysFont(None, 75)

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

racket1 = Player('racket.png', 30, 200, 50, 150,4)

racket2 = Player('racket.png', 620, 200, 50, 150,4)

clock = time.Clock()
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        
        window.blit(background, (0, 0))
        
        racket1.update1()
        racket1.reset()
        racket2.update2()
        racket2.reset()
        
    display.update()
    clock.tick(40)
