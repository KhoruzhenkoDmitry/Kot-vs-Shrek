from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption("tipo shuter")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
lost = 0
FPS = 144

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed
class enemy(GameSprite):
    def update(self):
        global lost
        if self.rect.y < 435:
            self.rect.y = self.rect.y + self.speed
        else:
            self.rect.y = -70
            self.rect.x = randint(20,450)
            lost = lost + 1

            
class Bullet(GameSprite):
    def Shot(self):
        keys = key.get_pressed()
        if 1 == 1:
            pass
monsters = sprite.Group()
for i in range(1,6):
    monster=enemy("ufo.png",randint(50,650),10,randint(1,3))
    monsters.add(monster)
player = Player("rocket.png", 350, 400, 7)
font.init()
font = font.Font(None, 35)
game = True
while game:
    clock = time.Clock()
    clock.tick(FPS)
    player.update()
    monsters.update()
    window.blit(background,(0, 0))
    lose = font.render('Пропущено: '+str(lost),1,(255,255,255))
    window.blit(lose,(5,25))
    player.reset()
    monsters.draw(window)

    for i in event.get():
        if i.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    display.update() 
