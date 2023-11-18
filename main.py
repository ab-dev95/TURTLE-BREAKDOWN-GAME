from turtle import Screen, TK
from classes import *
import time


screen = Screen()
screen.setup(height=500, width=865)
screen.title('Breakout Game')
screen.bgcolor('black')
screen.tracer(0)


player = Player()
ball = Ball()
lives = Score(4, 'l')
score = Score(0, 'r')
green_blocks = Blocks('green', -30)
yellow_blocks = Blocks('yellow', 20)
orange_blocks = Blocks('orange', 70)
red_blocks = Blocks('red', 120)
screen.update()


game = True
collusion = False
speedy = 0.09
player.player.ondrag(player.player_drag)


while game:
    time.sleep(speedy)
    ball.ball_move(game)
    screen.update()

    if ball.ball.xcor() > 400 or ball.ball.xcor() < -400:
        ball.bounce_x()

    if ball.ball.ycor() > 240:
        ball.bounce_y()
    
    if ball.ball.ycor() < -240:
        lives.num -= 1
        lives.update_score()
        time.sleep(1)
        ball.reset()
    
    if lives.num < 0:
        game = False
        TK.messagebox.showinfo(title='Game Over', message=f'Score: {score.num}')
        screen.bye()

    for i in green_blocks.bks:
        if ball.ball.distance(i) < 42:
            i.hideturtle()
            green_blocks.bks.remove(i)
            collusion = True
            score.num += 4
            score.update_score()
    
    for i in yellow_blocks.bks:
        if ball.ball.distance(i) < 42:
            i.hideturtle()
            yellow_blocks.bks.remove(i)
            collusion = True
            score.num += 4
            score.update_score()

    for i in orange_blocks.bks:
        if ball.ball.distance(i) < 42:
            i.hideturtle()
            orange_blocks.bks.remove(i)
            collusion = True
            score.num += 4
            score.update_score()

    for i in red_blocks.bks:
        if ball.ball.distance(i) < 42:
            i.hideturtle()
            red_blocks.bks.remove(i)
            collusion = True
            score.num += 4
            score.update_score()
    
    if ball.ball.distance(player.player) < 25:
        collusion = True
        speedy = 0.05
    
    if collusion:
        ball.bounce_y()
        collusion = False