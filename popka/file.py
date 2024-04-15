from pygame import *

window = display.set_mode((500, 400))
display.set_caption('Пинг-понг')

class GameSprite(sprite.Sprite):
    def __init__(self, x, y, weight, height):
        super().__init__()
        self.x = x
        self.y = y
        self.w = weight
        self.h= height
        self.image = transform.scale(image.load(img),(self.w, self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        def rendering(self):
            window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(Gamesprite):
    def __init__(self, x, y, weight, height):
        super().__init__()
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        pass    


class Rocket(GameSprite):





roket1 = Rocket('rocket.png', 20, 200, 20, 100, 2)
roket2 = Rocket('rocket.png', 680, 200, 20, 100, 2)
ball = Ball('tennis.png', 350, 250, 20, 20, 2, 2)




clock = time.Clock(Fps)

game = True

while game:

    for e in event.get():
        if e . type == QUIT:
            game = False
    rocket1.rendering()
    rocket2.rendering()
    ball.rendering()


    clock.tick(60)
    display.update()

