#PING PONG

from pygame import *
from random import randint

win_width = 700
win_height = 500

font.init()
font2 = font.SysFont("Arial", 36)

window = display.set_mode((win_width,win_height))
display.set_caption("Ping Pong")
background = transform.scale(image.load("Теннисный корт_ стоковые векторные изображения, иллюстрации _ Depositphotos.png"), (win_width,win_height))

run = True
finish = False
clock = time.Clock()
FPS = 60

#mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    



 = Player("rocket.png", 5, win_height - 100, 10, 80, 100)
monsters = sprite.Group()
for f in range(5):
    monster = Enemy('ufo.png', randint(80, win_width- 80), -50, 2, 80, 50)
    monsters.add(monster)"""





finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0, 0))
        """ship.update()
        ship.reset()

        monsters.update()
        monsters.draw(window)
        bullets.update()
        bullets.draw(window)
        
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 50))"""

        
        clock.tick(FPS)
        display.update()

    time.delay(50)
