from pygame import *

win_widht = 700
win_height = 500
back = (200, 50, 70)
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
window.fill(back)

speed_x = 3
speed_y = 3

run = True
finish = False
clock = time.Clock()
FPS = 60 

# font.init()
# font = font.Font(None,70)
# win = font.render("YOU WIN!",True,(255,215,0))
# lose = font.render('BRUH YOU LOSE!',True,(180,0,0))

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed, player_width, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_right(self): 
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_height - 100:
            self.rect.y += self.speed
    def update_left(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_height - 100:
            self.rect.y += self.speed

player1 = Player('forpingpong.png',10,200,4, 30, 100)
player2 = Player('forpingpong.png',660,200,4, 30, 100)
ball = GameSprite('circle2-transformed.png',220, 320,4,70,70)

while run:
    for e in event.get():
        if e.type == QUIT:
            run  = False
    
    if not finish:
        window.fill(back)
        player1.update_left()
        player2.update_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(player1,ball) or sprite.collide_rect(player2,ball):
            speed_x = speed_x * -1
        
        if ball.rect.y > win_height-70 or ball.rect.y < 0:
            speed_y = speed_y * -1
        

        player1.reset()  
        player2.reset() 
        ball.reset()

    display.update()
    clock.tick(FPS)