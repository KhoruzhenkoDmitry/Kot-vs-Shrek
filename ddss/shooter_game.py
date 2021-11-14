from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption("Shrek_Shuter")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
keys = key.get_pressed()
num_fire = 0
rel_time = False
lost = 0
c = 0

FPS = 144
bullets = sprite.Group()

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
    def fire(self):
        bullet = Bullet('bullet.png', player.rect.centerx, player.rect.top, 10)
        bullets.add(bullet)
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
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
    
monsters = sprite.Group()
for i in range(1,6):
    monster=enemy("shrek.png",randint(50,650),10,randint(1,3))
    monsters.add(monster)
player = Player("bob.png", 350, 400, 7)
font.init()
font = font.SysFont("Arial", 35)
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
    bullets.update()
    bullets.draw(window)

    if rel_time == True:
        now_time = timer()
        if now_time - last_time<3:
            reload = font.render("Перезарядись, пжпжпж")

    collide = sprite.groupcollide(monsters, bullets, True, True)
    for i in collide:
        monster=enemy("shrek.png",randint(50,650),10,randint(1,3))
        monsters.add(monster)

    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.fire()
                num_fire = num_fire + 1
    display.update()