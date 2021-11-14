from pygame import *


window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"), (700, 500))
FPS = 60

#kick = mixer.Sound('kick.ogg')
#money = mixer.Sound('money.ogg')

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()

mixer.music.load("kick.ogg")
mixer.music.load("money.ogg")

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (85, 24, 255))
lose = font.render('YOU LOSE', True, (255, 39, 24))

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
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.col_1 = color_1
        self.col_2 = color_2
        self.col_3 = color_3
        self.image = Surface((wall_width, wall_height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
wall_1 = Wall(54, 255, 24, 200, 60, 450, 10)
wall_2 = Wall(54, 255, 24, 150, 480, 350, 10)
wall_3 = Wall(54, 255, 24, 300, 20, 10, 380)
player = Player("hero.png", 65, 65, 10) 
enemy = Enemy("cyborg.png", 150, 150, 10)
treasure = GameSprite("treasure.png", 625, 375, 10)

finish = False

game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        enemy.update()

    clock = time.Clock()
    player.reset()
    enemy.reset()
    treasure.reset()

    wall_1.draw_wall()
    wall_2.draw_wall()
    wall_3.draw_wall()

    player.reset()
    enemy.reset()
    treasure.reset()

    if sprite.collide_rect(player, enemy)or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3):
        finish = True
        window.blit(lose, (200, 200))
        #kick.play()
    
    if sprite.collide_rect(player, treasure):
        finish = True
        window.blit(win, (200, 200))
        #money.play()
    display.update()
    clock.tick(FPS)