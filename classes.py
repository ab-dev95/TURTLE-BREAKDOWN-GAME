from turtle import Turtle, ondrag, speed
import random


class Player():
    
    def __init__(self):
        self.player = Turtle()
        self.player.shape('square')
        self.player.color('blue')
        self.player.shapesize(0.5, 3)
        self.player.penup()
        self.player.setposition(0, -210)
        self.player.speed(10) 
    
    def player_drag(self, x, y): 
        self.player.ondrag(None)  
        self.player.setposition(x, -215) 
        self.player.ondrag(self.player_drag) 
        

class Ball():

    def __init__(self):
        self.ball = Turtle()
        self.ball.shape('circle')
        self.ball.color('white')
        self.ball.penup()
        self.ball.setposition(0, -190)
        self.x = 10
        self.y = 10
    
    def ball_move(self, game): 
        game = game
        new_x = self.ball.xcor() + self.x
        new_y = self.ball.ycor() + self.y
        self.ball.setposition(new_x, new_y)
    
    def bounce_x(self):
        self.x *= -1
    
    def bounce_y(self):
        self.y *= -1
    
    def reset(self):
        self.ball.setposition(0, -190)
        self.x = 10
        self.y = 10


class Score():

    def __init__(self, num, pos):
        self.score = Turtle()
        self.score.color('white')
        self.score.penup()
        self.score.hideturtle()
        if pos == 'l':
            self.score.setposition(-400, 200)
        else:
            self.score.setposition(360, 200)
        self.num = num
        self.score.write(self.num, align='left', font=('comic', 18, 'normal'))
    
    def update_score(self):
        self.score.clear()
        self.score.write(self.num, align='left', font=('comic', 18, 'normal'))


class Blocks():

    def __init__(self, color, y):
        self.all_blocks = [2,2,2,2, 3,3,3,3, 4,4,4,4]
        self.color = color
        self.x = -432
        self.y = y
        self.bks = []
        self.create_block()
    
    def equal_blocks(self):
        width = random.randint(2, 4)
        if width in self.all_blocks:
            self.all_blocks.remove(width)
        else:
            while width not in self.all_blocks:
                width = random.randint(2, 4)
            self.all_blocks.remove(width)
        return width
    
    def create_block(self):
        new_width = 0
        while len(self.all_blocks) != 0:
            width = self.equal_blocks()
            self.block = Turtle()
            self.block.shape('square')
            self.block.shapesize(2, width)
            self.block.color(self.color)
            self.block.penup()
            self.x += (new_width * 10) + (width * 10) + 10
            self.block.setposition(self.x, self.y)
            new_width = width
            self.bks.append(self.block)