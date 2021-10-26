from turtle import *
from random import *
import time
player = Turtle()
screen = Screen()
player.shape("circle")
hideturtle()
player.go = None
player.color("green")
player.penup()
player.goto(-20,30)
player.shape("circle")
hideturtle()
collectpurple = Turtle()
collectpurple.shape("circle")
collectpurple.color("purple")
collectpurple.penup()
collectpurple.goto(-120,90)
def up():
    if player.go != "down":
        player.sety(player.ycor() + 20)

def down():
    if player.go != "up":
        player.sety(player.xcor() - 20)

def left():
    if player.go != "left":
        player.setx(player.xcor() - 20)

def right():
    if player.go != "right":
        player.setx(player.xcor() + 20)
score_board = Turtle()
score_board.speed(0)
score_board.color("black")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 165)
score_board.clear()
score_board.write("Score: 0", align="center", font=("Courier", 19, "normal"))
score = 0
game_over = Turtle()
game_over.speed(0)
game_over.color('black')
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 100)
game_over.clear()
color(randint(0, 105), randint(0, 235),randint(0, 255))
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
screen.onkey(up, 'w')
screen.onkey(down, 's')
screen.onkey(left, 'a')
screen.onkey(right, 'd')
enemy = []
old_score = 0
while True:
    screen.update()
    if old_score != score:
        new_enemy = Turtle()
        new_enemy.shape('circle')
        new_enemy.speed(0)
        new_enemy.penup()
        new_enemy.goto(0, 60)
        new_enemy.color('red')
        new_enemy.clear()
        enemy.append(new_enemy)
    x = randint(-130, 100)
    y = randint(-130, 234)
    if player.distance(collectpurple) < 20:   
        collectpurple.goto(x,y)
        score += 1 
        old_score += score-1
        score_board.clear()
        score_board.write('Score: {}'.format(score), align="center", font=("Courier", 24, "normal"))
    idk = 0
    idk_2 = 0
    idk += 1
    idk_2 += idk+1
    for enemy_ in enemy:
        enemy_.goto(x+idk_2, y+idk)
        if enemy_.distance(player) < 20:  
            score_board.clear()
            score_board.write('Game ended', align="center", font=("Courier", 24, "normal"))
            time.sleep(0.80)
            score_board.clear()
            score_board.write('Score: 0', align="center", font=("Courier", 24, "normal"))
    
done()
