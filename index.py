from pygame import *

win_widht = 700
win_height = 500
back = (200, 50, 70)
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
window.fill(back)

speed_x = 3
speed_y = 3

run = True
finish = False
clock = time.Clock()
FPS = 60 

point1 = 0
point2 = 0

font.init()
font1 = font.Font(None,35)
score1 = font1.render("Баллы1: " + str(point1) ,True,(0,0,0))
score2 = font1.render("Баллы2: " + str(point2) ,True,(0,0,0))
lose1 = font1.render("Игрок 1 проиграл",True,(0,0,0))
lose2 = font1.render("Игрок 2 проиграл",True,(0,0,0))

 


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
ball = GameSprite('circle.png',220, 320,4,70,70)

wait = 0

while run:
    if wait == 0:
        wait = 300
        if speed_x > 0:
            speed_x += 1
        else:
            speed_x -= 1
        if speed_y > 0:
            speed_y += 1
        else:
            speed_y -= 1
    else:
        wait -= 1
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
            speed_x *= -1
        
        if ball.rect.y > win_height-70 or ball.rect.y < 0:
            speed_y *= -1 

        if ball.rect.x < 0:
            finish = True
            point2 += 1
            score2 = font1.render("Баллы2: " + str(point2) ,True,(0,0,0))
            time.delay(1000)

        if ball.rect.x > win_widht:
            finish = True
            point1 += 1 
            score1 = font1.render("Баллы1: " + str(point1) ,True,(0,0,0))
            time.delay(1000)

        window.blit(score1,(10,0))
        window.blit(score2,(550,0))

        player1.reset()  
        player2.reset() 
        ball.reset()

    else: 
        finish = False
        speed_x = 3
        speed_y = 3
        ball = GameSprite('circle.png', 220,320,4,70,70)
        
    display.update()
    clock.tick(FPS) 